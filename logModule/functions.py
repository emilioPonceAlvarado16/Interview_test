import re
from datetime import datetime

def format_validator(day_record:str):
    """
        this function will validate if the "day_record" follows the right format.

        input:
            String of the day record.
            Example: "MO10:00-12:00"   
        checks:
            * Validates the format using regular expressions.
            * start_time must be greater than end_time.
        return:
            * Day:string, start_time:datetime, end_time:datetime, which are extracted from the param.
        error handling:
            * raises RuntimeError if is not a correct format or if the time range is not valid.
      
  
    """
    pattern=r"^(MO|TU|WE|TH|FR|SA|SU)([0-1][0-9]|[2][0-3]):([0-5][0-9])\s*-\s*([0-1][0-9]|[2][0-3]):([0-5][0-9])$"
    groups=re.search(pattern, day_record)
    
    if(not groups):
        raise RuntimeError("Day record format is incorrect, please check this ==> "+"\033[1;31;48m"+day_record+"\033[1;33;48m") 

    groups=groups.group(1,2,3,4,5)
   

    day=groups[0]
    start="{}:{}".format(groups[1],groups[2])
    end="{}:{}".format(groups[3],groups[4])
    start_time=datetime.strptime(start, '%H:%M')
    end_time=datetime.strptime(end, '%H:%M')

    if(start_time>end_time):
        raise RuntimeError("\033[1;31;48m"+"Not valid range: start: {} is greather than end: {}".format(start_time.strftime("%H:%M"), end_time.strftime("%H:%M"))+"\033[1;33;48m")


    return day,start_time,end_time

def is_a_match(start1:datetime, end1:datetime,start2:datetime,end2:datetime)->bool:
    """
        This function will compare two datetime ranges
        and determine if is a match or not
        Ex1: range1: 10:00-12:00 && range2:11:00-13:00 will return True
        Ex2: range1: 10:00-12:00 && range2:12:02-13:00 will return False

    """
    if(start2<start1):
         return end2>=start1
    elif(start1<start2):
        return end1>=start2
    else:
        return True
    
def file_to_records(filename:str)->list:

    """
        This function will read a file which contains the logs, 
            process it and convert it into a list of dictionaries.

        input: name of the file which contains the logs.

        return: 
            * List of dictionaries
            Example: [{'RENE'}:{'MO':{'start':'10:00','end':'12:00'}, ...},{'JUAN':{...]
            Hint: the time is actually in datetime data type

        error handling:
            * raises ValueError if the param is invalid.
            * raises RunTimeError:
                - If there is a problem when reading the file: Non-existing file, blocked, no access, etc.
                - RunTimeError catched from the format_validator function.
                - If there are two or more records with the same within the same person.


    """

    if( type(filename)!=str):
        raise ValueError("Param of file_to_records(filename) must be a string")
    try:
        file=open(filename,"r")
    except OSError:
        raise RuntimeError("\033[1;31;48m"+"Failed to open {}".format(filename))
    

    records_list=[]
    lines=file.readlines()
    file.close()
    records_list=[]
    pre_register=dict()
    for line in lines:
        if(line!="\n"):
            line_=line.strip("\n")
            line_l=line.split("=")
            
            n_line=len(line_l)

            if(n_line!=2):
                raise RuntimeError("\033[1;33;48m"+"Wrong format of the log, please check {}".format(line))
            name=line_l[0]
            record=line_l[1]
            if(len(name)==0 or name=="" or len(record)==0 or record==""): 
                raise RuntimeError("\033[1;33;48m"+"Wrong format of the log, please check {}".format(line))
            pre_register[name]= dict()
           
            for day_record in record.split(","):
                day_record=day_record.strip(" ")
                try:
                    day,start1,end=format_validator(day_record)   
                except RuntimeError as error:
                    raise RuntimeError("Exception catched from the format_validator\n")

                if(day in pre_register[name].keys()):raise RuntimeError("\033[1;33;48m"+"Error: Encountered two or more records with the same day of the week within the same person! {}".format(line))

                pre_register[name][day]={"start":start1,"end":end}
            
        
            records_list.append({name:pre_register[name]})
    return records_list



def find_matches(person1:dict, person2:dict)->tuple:

    """
        this function recevies two dictionaries that represents the logs of two persons along the week.

            return:
                * Returns a tuple of the numbers of matches within the same time range and their names in pair.
                Example:  ('ASTRID-RENE', 2)

    """
   
    dicctionary=dict()
    name1=list(person1.keys())[0]
    name2=list(person2.keys())[0]
    person1=person1[name1]
    person2=person2[name2]
    pair_names="{}-{}".format(name2,name1)
    for key, value in person1.items():
        if(key in person2.keys()):
            records_person1=person1[key]
            records_person2=person2[key]
            match=is_a_match(records_person1["start"], records_person1["end"],records_person2["start"], records_person2["end"])
            if(match):
                
                if(pair_names not in dicctionary):
                    dicctionary[pair_names]=1
                else:
                    dicctionary[pair_names]=dicctionary[pair_names]+1
    return (pair_names,dicctionary[pair_names])  

def get_results(records_list:list)->list:

    """ 
        This function receives a list of dictionaries which represents the logs, 
            process it and then return a list of tuples. ("pair-names", n_matches).
            
           Compare each employee with the others employees and determine the number of matches between them.
                
        return:
            Example: [('ASTRID-RENE', 2), ('ANDRES-RENE', 2), ('ANDRES-ASTRID', 3)]

    """

    n_records=len(records_list)
    
    results=[]
    for idx in range(n_records):
        for idy in range(idx, n_records-1):
            di=find_matches( records_list[idx], records_list[idy+1])
            results.append(di)

    return results

def results_to_string(results:list)->str:

    """
        This function will convert a list of tuples [(a,b),...] 
        
        into a single string "a:b \ n..."
        

    """
    assert type(results)==list, "\033[1;33;48m"+"Param of results_to_string() must be a list"
    st=""
    n_results=len(results)
    for i in range(n_results):
        result=results[i]
        if(i==n_results-1):
            st=st+"{}:{}".format(result[0],result[1])
        else:
            st=st+result[0]+":"+str(result[1])+"\n"
    return st
