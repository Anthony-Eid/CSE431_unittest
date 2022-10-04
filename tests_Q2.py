from unittest import TestCase
from test_functions import run_test, get_args_data
from Q2 import main


rel_path = 'case_files/Q2/'

class Test(TestCase):
        
    def test_example0(self):
        
        input_args, expected_outputs = get_args_data(rel_path, 0)
        run_test(input_args, expected_outputs, main)
    
    def test_example1(self):
        
        input_args, expected_outputs = get_args_data(rel_path, 1)
        run_test(input_args, expected_outputs, main)
        
    def test_example2(self):
        
        input_args, expected_outputs = get_args_data(rel_path, 2)
        run_test(input_args, expected_outputs, main)
    
    def test_example3(self):
        
        input_args, expected_outputs = get_args_data(rel_path, 3)
        run_test(input_args, expected_outputs, main)
    
    def test_example4(self):
        
        input_args, expected_outputs = get_args_data(rel_path, 4)
        run_test(input_args, expected_outputs, main)
    

