import re
from datetime import datetime

def format_validator(time):
    
    pattern=r"^(MO|TU|WE|TH|FR|SA|SU)([0-1][0-9]|[2][0-3]):([0-5][0-9])\s*-\s*([0-1][0-9]|[2][0-3]):([0-5][0-9])$"
    groups=re.search(pattern, time)
    if(not groups):return False #if Empty search, then return False

    groups=groups.group(1,2,3,4,5)
    day=groups[0]
    start="{}:{}".format(groups[1],groups[2])
    end="{}:{}".format(groups[3],groups[4])
    start_time=datetime.strptime(start, '%H:%M')
    end_time=datetime.strptime(end, '%H:%M')

    if(start_time>end_time):return False #if start time is greater than end time, then return False

   
    return day,start_time,end_time

def is_time_match(start1, end1,start2,end2):
    
    if(start2<start1):
         return end2>=start1
    elif(start1<start2):
        return end1>=start2
    else:
        return True
    

file=open("hola.txt","r")

time="MO10:00-12:00"


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
           
            
            day,start1,end=format_validator(day_record)            
            pre_register[name][day]={"start":start1,"end":end}
            
        
        records_list.append({name:pre_register[name]})
        
dic=[{'RENE': {'MO': {'start': '10:00', 'end': '12:00'}, 'TU': {'start': '10:00', 'end': '12:00'}, 'TH': {'start': '01:00', 'end': '03:00'}, 'SA': {'start': '14:00', 'end': '18:00'}, 'SU': {'start': '20:00', 'end': '21:00'}}}, {'ASTRID': {'MO': {'start': '10:00', 'end': '12:00'}, 'TH': {'start': '12:00', 'end': '14:00'}, 'SU': {'start': '20:00', 'end': '21:00'}}}, {'ANDRES': {'MO': {'start': '10:00', 'end': '12:00'}, 'TH': {'start': '12:00', 'end': '14:00'}, 'SU': {'start': '20:00', 'end': '21:00'}}}]



def find_matches(person1, person2):
    dicctionary=dict()
    name1=list(person1.keys())[0]
    name2=list(person2.keys())[0]


    for key, value in person1[name1].items():
        if(key in person2[name2].keys()):
            records_person1=person1[name1][key]
            records_person2=person2[name2][key]
            match=is_time_match(records_person1["start"], records_person1["end"],records_person2["start"], records_person2["end"])
            if(match):
                
                pair_names=name2+"-"+name1
                if(pair_names not in dicctionary):
                    dicctionary[pair_names]=1
                else:
                    dicctionary[pair_names]=dicctionary[pair_names]+1
    return dicctionary



    

si=find_matches(dic[0], dic[1])
print(si)
# print(records_list)



# print(is_time_match(start1, end1, start2, end2))



