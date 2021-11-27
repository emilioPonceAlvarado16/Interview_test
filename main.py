import sys
import re
from datetime import datetime
import os

def format_validator(time):
    
    pattern=r"^(MO|TU|WE|TH|FR|SA|SU)([0-1][0-9]|[2][0-3]):([0-5][0-9])\s*-\s*([0-1][0-9]|[2][0-3]):([0-5][0-9])$"
    groups=re.search(pattern, time)
    
    if(not groups):
        raise ValueError("Date format is incorrect, please check this ==> "+time) 

    groups=groups.group(1,2,3,4,5)
   

    day=groups[0]
    start="{}:{}".format(groups[1],groups[2])
    end="{}:{}".format(groups[3],groups[4])
    start_time=datetime.strptime(start, '%H:%M')
    end_time=datetime.strptime(end, '%H:%M')

    if(start_time>end_time):raise ValueError("Not valid range: start: {} is greather than end: {}".format(start_time.strftime("%H:%M"), end_time.strftime("%H:%M")))

   
    return day,start_time,end_time

def is_a_match(start1, end1,start2,end2):
    
    if(start1>end1):
        raise ValueError("Not valid range: start :{} is greather than end :{}".format(start1.strftime("%H:%M"), end1.strftime("%H:%M")))
    if(start2>end2):
        raise ValueError("Not valid range: start :{} is greather than end :{}".format(start2.strftime("%H:%M"), end2.strftime("%H:%M")))

    if(start2<start1):
         return end2>=start1
    elif(start1<start2):
        return end1>=start2
    else:
        return True
    
def file_to_records(filename="records.txt"):
    try:
        file=open(filename,"r")
    except OSError:
        raise RuntimeError("Failed to open {}".format(filename))
    

    records_list=[]
    lines=file.readlines()
    file.close()
    records_list=[]
    pre_register=dict()
    for line in lines:
        if(line!="\n"):
            line=line.strip("\n")
            line=line.split("=")
            name=line[0]
            record=line[1]
            pre_register[name]= dict()
        
            for day_record in record.split(","):
           
                try:
                    day,start1,end=format_validator(day_record)   
                except ValueError as error:
                    raise ValueError("Exception catched from the format_validator\n")
                    
                pre_register[name][day]={"start":start1,"end":end}
            
        
            records_list.append({name:pre_register[name]})
    return records_list



def find_matches(person1, person2):
  
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
    return (pair_names,dicctionary[pair_names])   #('ASTRID-RENE', 2)

def get_results(records_list):
    assert type(records_list)==list, "records_list must be a list"
    n_records=len(records_list)
    
    result=[]
    for idx in range(n_records):
        for idy in range(idx, n_records-1):
            di=find_matches( records_list[idx], records_list[idy+1])
            result.append(di)

    return result #[('ASTRID-RENE', 2), ('ANDRES-RENE', 2), ('ANDRES-ASTRID', 3)]

def results_to_string(results):
    assert type(results)==list , "results must be a list"
    
    st=""
    n_results=len(results)
    for i in range(n_results):
        result=results[i]
        if(i==n_results-1):
            st=st+"{}:{}".format(result[0],result[1])
        else:
            st=st+result[0]+":"+str(result[1])+"\n"
    return st


input="records.txt"
records=file_to_records(input)
results=get_results(records)
output=results_to_string(results)
print(output)

# print(results)

# results_to_string([])
