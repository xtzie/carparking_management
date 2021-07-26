## Requirements
- Ubuntu 16.04 or later
- Python 3 or later
- Additional Python library: ```hypothesis```

## Install Additional Library
Hypothesis library lets you write tests which are parametrized by a source of examples.  
To install, in the command line run:  
```pip install hypothesis```

## Bootstrap Data Usage
In the command line run:  
```python3 carparking_main.py -file "your_Car_Parking_File.txt"```  
  
Refer to ```sample_input.txt``` for example of data format.

## Property Testing
Testing program based on expected function properties. In the command line run:  
```python3 carparking_main_golden_testing.py```  
  
Example of property test:  
  
```some function```  

## Golden Testing
Testing program with stored output. In the command line run:  
```python3 carparking_main_golden_testing.py```   
  
Tests are stored in ```golden_unit_test_result``` folder  

## Implementation Assumptions

**Expected Input File Attributes:**
1. First line in format of: ```int int```
2. Subsequent lines should be in string format:  
```"Enter vehicle_type plate_number time"```  
OR  
```"Exit plate_number time"```  

Input File Assumptions
1. Format is as above.
2. Vehicle number plates are unique and distinct.
3. Entries and exits are sorted in ascending order.
4. Time in and out is formatted in seconds.

## Existing Extensibility
1. Space time complexity of o(k) for n inputs, with k being total number of vehicle lots.
2. Time complexity of o(n * k) for n inputs, with k being total number of vehicle lots.
3. Can instantiate with additional vehicle types and corresponding attributes.

## Future Design Extensibility
1. Build functionality to add / remove / block lots.
2. Push output into a database for data persistency
3. Mount onto docker image for production functionality





## Bootstrap Exception Handling
1. Exit time before entry time: Car remains in inventory, exit ignored.
2. First line inputs not non-negative integers: System exits.
3. Insufficient or excess variables: line skipped.
4. Time in incorrect format: line skipped.
5. Input other than "Enter"/"Exit" (e.g "Season_Entry", "Entry") : line skipped.
6. Input other than "Car"/"Motorcycle" (e.g "Bus") : line skipped.
7. Exiting vehicle not existing in car park: line skipped.
