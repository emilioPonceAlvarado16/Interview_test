import re
from datetime import datetime

def format_validator(time):
    
    pattern=r"^(MO|TU|WE|TH|FR|SA|SU)([0-1][0-9]|[2][0-3]):([0-5][0-9])\s*-\s*([0-1][0-9]|[2][0-3]):([0-5][0-9])$"
    groups=re.search(pattern, time)
    if(not groups):return False #Empty search, then return False

    groups=groups.group(1,2,3,4,5)
    day=groups[0]
    start="{}:{}".format(groups[1],groups[2])
    end="{}:{}".format(groups[3],groups[4])
    start_time=datetime.strptime(start, '%H:%M')
    end_time=datetime.strptime(end, '%H:%M')

    if(start_time>end_time):return False #Start time is greater than end time, then return False

   
    return day,start,end
    
file=open("hola.txt","r")

time="MO10:00-12:00"


lines=file.readlines()
file.close()

records_register=dict()
for line in lines:
    if(line!="\n"):
        #print(line)
        line=line.strip("\n")
        line=line.split("=")
        name=line[0]
        record=line[1]
        records_register[name]= dict()
        for day_record in record.split(","):
            #print(day_record)
            day,start1,end=format_validator(day_record)
            #{day:{"start":start1,"end":end}}
            
            records_register[name][day]={"start":start1,"end":end}
#print(records_register)

dic={'RENE': {'MO': {'start': '10:00', 'end': '12:00'}}, 'ASTRID': {'MO': {'start': '10:00', 'end': '12:00'}}, 'ANDRES': {'MO': {'start': '10:00', 'end': '12:00'}}}
def find_matches(dictionary):
    match=dict()
    for key,value in dictionary.items():
        print(key,value)
        pass

    

find_matches(records_register)
start2="10:04"
end2="23:02"

start1="10:05"
end1="23:30"

start1=datetime.strptime(start1, '%H:%M')
end1=datetime.strptime(end, '%H:%M')
start2=datetime.strptime(start2, '%H:%M')
end2=datetime.strptime(end2, '%H:%M')

def is_time_match(start1, end1,start2,end2):
    
    if(start2<start1):
         return end2>=start1
    elif(start1<start2):
        return end1>=start2
    else:
        return True
    

print(is_time_match(start1, end1, start2, end2))


