from logModule.functions import *

def main(input):
   
    records=file_to_records(input)
    results=get_results(records)
    output=results_to_string(results)
    return output
    


if __name__ == "__main__":
    
    filename="./logs/records.txt"
    #filename="./logs/records1.txt"
    output=main(filename)
    print(output)
