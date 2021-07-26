## Requirements
- Ubuntu 16.04 or later
- Python 3 or later
- Hypothesis property testing library

## Install Additional Libraries
```pip install hypothesis```

## Bootstrap Usage
```python3 carparking_main.py -file "your_Car_Parking_File.txt"```   
Refer to ```sample_input.txt``` for example of data format.

# Property Testing
Testing program based on expected function properties.
```python3 carparking_main_golden_testing.py``` 

## Golden testing
Testing program with stored output.  
```python3 carparking_main_golden_testing.py```   

Define carpark_attributes variables in ```config.json5```   
Attributes in the form: ```[vehicle_type: str, lots_available: int, fees: int]```
```
{
  "carpark_attributes": [
    ["car", 3, 2],
    ["motorcycle", 4, 1]
  ]
} 
```

## Files
1. carparking_main.py: Main file with Carpark() class
2. carparking_main_test.py: File to run unit tests for carparking_main.py
3. sample_input.txt: Sample input for carparking_main.py
4. unit_test: Folder of unit tests to test program functionality
5. result_unit_test: Folder of expected results of unit tests

## Usage
1. Run file in the python3 environment:
python3 carparking_main.py --Car_Parking_File 'your_Car_Parking_File.txt'
2. To run unit tests:
python3 carparking_main_test.py
3. To run from API:
from carparking_main import *
setup


Input File Attributes
1. File should be in .txt format
2. First line in format of: int int
3. Subsequent lines should be in string format:
'Enter Vehicle Type Plate_Number Time'
OR
'Exit Plate_Number Time'

Input File Assumptions
1. Format is as above.
2. Vehicle number plates are unique and distinct.
3. Entries and exits are sorted in ascending order.
4. Time in and out is formatted in seconds.


===============================================================================
Implementation Considerations

===============================================================================

Design Extensibility
1. Variables as object attributes (carFees, hourConversion)
2. Each vehicle entry as a modular function
 - single data structure
 - streamline functions
 
3. Space time complexity of o(1) for n inputs.
4. Time complexity of o(n * k) for n inputs, with k being total number of vehicle lots.
5. Able to add / remove / block lots - Status of lots - give distinct open lot
6. separate configurations file - no code update to production server - maintain code consistency - build to local environment then staging then production (using same source code)
docker image ensures hash is the same
yaml json properties file 



Exception Handling
1. Exit time before entry time: Car remains in inventory, exit ignored.
2. First line inputs not non-negative integers: System exits.
3. Insufficient or excess variables: line skipped.
4. Time in incorrect format: line skipped.
5. Input other than "Enter"/"Exit" (e.g "Season_Entry", "Entry") : line skipped.
6. Input other than "Car"/"Motorcycle" (e.g "Bus") : line skipped.
7. Exiting vehicle not existing in car park: line skipped.
8. 

Good Programming Practices and Tests
1. 

Code Packaging & Project Structure
1. 
##########error handling should print out stuff
