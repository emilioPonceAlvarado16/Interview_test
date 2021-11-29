import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname("../"))
from logModule.functions import *
import unittest
from main import main

class TestLogModule(unittest.TestCase):
    def test_invalid_filename(self):

        
        self.assertRaises(RuntimeError,file_to_records, "../imaginary_folder/non_existing_record.txt") #Wrong path, non existing file

        #Invalid inputs
        self.assertRaises(ValueError,file_to_records, 4) 
        self.assertRaises(ValueError,file_to_records, [])
        self.assertRaises(ValueError,file_to_records, -1)
        self.assertRaises(ValueError,file_to_records, 4+2j)
        self.assertRaises(ValueError,file_to_records, {"test":4})
    

    def test_invalid_log_file(self):
       
        invalid_files_list=["log1.txt", "log2.txt","log3.txt","log4.txt","log5.txt"]  #List of invalid log files
        for filename in invalid_files_list:
            filename="../fake_logs/{}".format(filename)
            self.assertRaises(RuntimeError,main, filename)

    def test_format_validator(self):

        self.assertRaises(RuntimeError, format_validator, "MO10:10-45:54") #Invalid hour 45:54
        self.assertRaises(RuntimeError, format_validator, "ZO10:10-11:54") #Invalid day of the week
        self.assertRaises(RuntimeError, format_validator, "TU11:20-10:54") #Invalid range
        self.assertRaises(RuntimeError, format_validator, "MO85:10-45:54") #Invalid hour 85:10
        self.assertRaises(RuntimeError, format_validator, "MO cd45:54") #Invalid record 
        self.assertRaises(RuntimeError, format_validator, "kdmkdcmkdcm") #Invalid record 

        #Expected output from format_validator
        self.assertEqual(format_validator("TU10:10-11:54"), ("TU", datetime.strptime("10:10", '%H:%M'),datetime.strptime("11:54", '%H:%M'))) #Expected output 
        self.assertEqual(format_validator("MO10:10-11:54"), ("MO", datetime.strptime("10:10", '%H:%M'),datetime.strptime("11:54", '%H:%M'))) #Expected output 
        self.assertEqual(format_validator("FR10:10-11:54"), ("FR", datetime.strptime("10:10", '%H:%M'),datetime.strptime("11:54", '%H:%M'))) #Expected output 
        self.assertEqual(format_validator("TH10:10-11:54"), ("TH", datetime.strptime("10:10", '%H:%M'),datetime.strptime("11:54", '%H:%M'))) #Expected output 
        self.assertEqual(format_validator("SU10:10-11:54"), ("SU", datetime.strptime("10:10", '%H:%M'),datetime.strptime("11:54", '%H:%M'))) #Expected output 
        self.assertEqual(format_validator("SA10:10-11:54"), ("SA", datetime.strptime("10:10", '%H:%M'),datetime.strptime("11:54", '%H:%M'))) #Expected output 

    def test_expected_output(self):

        #Expected output from main()
        expected_output1="""ASTRID-RENE:2\nANDRES-RENE:2\nANDRES-ASTRID:3"""
        self.assertEqual(main("../logs/records.txt"), expected_output1)

        expected_output2="""ASTRID-RENE:3"""
        self.assertEqual(main("../logs/records1.txt"), expected_output2)


if __name__ == "__main__":
    unittest.main()
