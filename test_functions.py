"""
By Anthony Eid 

File contains functions that help test code in CSE 431 at MSU.
"""

from unittest.mock import patch, Mock
from unittest import TestCase

from typing import List, Tuple, Any

import os

path = os.path.dirname(__file__)

def run_test(input_list, output_list, func):
    """Run unittests on a function.
    
    This function mocks input() and print() to control what input() 
    outputs, and to save what func has printed while it ran.

    Args:
        input_list (_type_): The list of input variables
        output_list (_type_): The list of expected outputs
        func (_type_): The function to run the test on
    """
    with patch('builtins.input', side_effect = input_list) as mock_input,\
            patch('builtins.print') as mock_output:
        
        test = TestCase()
        
        func()
        call_list = mock_output.call_args_list
        
        test.assertEquals(len(call_list), len(output_list))
        i = 0
        for call, expected_call in zip(call_list, output_list):
            TestCase.assertEquals(TestCase(), str(call[0][0]), str(expected_call))
            i += 1


def get_args_data(rel_path: str, file_num: int) -> Tuple[List[Any], List[Any]]:
    """This function creates two lists of inputs and expected outputs to
    use as arguments in function run_tests().

    Args:
        rel_path (str): The path of the directory that houses test case files.
        file_num (int): The number of the test case file you wish to run

    Returns:
        Tuple[List[Any], List[Any]]: A tuple containing input and output lists
        from the cases files. Index 0 is the input_args list, Index 1 is the 
        output_args list.
    """
    
    
    # Create the correct file path to read from
    str_num = str(file_num) if file_num >= 10 else '0' + str(file_num)
    str_num += '.txt'
    
    files_path = os.path.join(path, rel_path)
    
    # Open files and convert them to lists
    input_args = open(os.path.join(files_path + 'input' + str_num), 'r').read()
    output_args = open(os.path.join(files_path + 'output' + str_num), 'r').read()
    
    input_args = input_args.splitlines()
    output_args = output_args.splitlines()
    
    # Get rid of any empty inputs
    if len(output_args) > 0 and output_args[-1] == "":
        output_args.pop(-1)
        
    return input_args, output_args