from logModule.functions import *

if __name__ == "__main__":
    input="records.txt"
    records=file_to_records(input)
    results=get_results(records)
    output=results_to_string(results)
    print(output)

