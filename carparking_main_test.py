from carparking_main import BootstrapData
import sys
import filecmp
import os

unit_test_filepath = './unit_test'
comparison_filepath = './result_unit_test'
original_stdout = sys.stdout
passed = 0

for file in os.listdir(unit_test_filepath):
    
    with open(unit_test_filepath + '/' + file, 'r') as file_lines:
        with open('temp.txt', 'w') as w:
            sys.stdout = w
            BootstrapData(file_lines)
            sys.stdout = original_stdout

    if filecmp.cmp('temp.txt', comparison_filepath + '/result_' + file):
        print(file, ' Passed!')
        passed += 1
    else:
        print(file, ' Failed.')

cases = len(os.listdir(unit_test_filepath))
print(f'{passed}/{cases} Passed')
os.remove('temp.txt')
