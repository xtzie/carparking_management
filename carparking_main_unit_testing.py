import pytest
from carparking_main import Carpark
import math

# In the format type, lots available, fee per hour
carpark_attribute_map = [('car', 3, 2), ('motorcycle', 4, 1)]

carpark1 = Carpark(carpark_attribute_map, fee_time_block=3600)

def test_motorcycle_entry():
    assigned, time_in, veh_type = carpark1.vehicle_entry('motorcycle', 'SGX1234A', 1613541902)
    assert assigned + 1 == 1
    assert time_in == 1613541902
    assert veh_type == 'motorcycle'

def test_car_entry():
    assigned, time_in, veh_type = carpark1.vehicle_entry('car', 'SGF9283F', 1613541902)
    assert assigned + 1 == 1
    assert time_in == 1613541902
    assert veh_type == 'car'

def test_assignment1():
    assigned, time_in, veh_type = carpark1.vehicle_entry('car', 'SGP2937F', 1613546029)
    assert assigned + 1 == 2
    assert time_in == 1613546029
    assert veh_type == 'car'

def test_assignment2():
    assigned, time_in, veh_type = carpark1.vehicle_entry('car', 'SDW2111W', 1613549730)
    assert assigned + 1 == 3
    assert time_in == 1613549730
    assert veh_type == 'car'

def test_rejection():
    rejection = carpark1.vehicle_entry('car', 'SSD9281L', 1613549740)
    assert rejection == 'Rejected'

def test_exit_before_entrytime():
    plate, exit_time = 'SGX1234A', 1613541902 - 100
    statement = carpark1.vehicle_exit(plate, exit_time)
    assert carpark1.vehicleMap[plate][2] == 'motorcycle'
    assert carpark1.vehicleMap[plate][1] == 1613541902
    assert carpark1.vehicleMap[plate][0] == 0
    assert statement == 'Rejected exit. Vehicle SGX1234A exit time of 1613541802 earlier than entry time of 1613541902.'

def test_phantom_exit():
    plate, exit_time = 'Phantom', 1613541902
    Rejection = carpark1.vehicle_exit(plate, exit_time)
    assert Rejection == 'Rejected exit, vehicle does not exist'

def test_exit1():
    plate, exit_time = 'SGX1234A', 1613545602
    vehicle_type, plate, billed = carpark1.vehicle_exit(plate, exit_time)
    assert vehicle_type == 'motorcycle'
    assert plate == 'SGX1234A'
    assert billed == 2

def test_exit2():
    plate, exit_time = 'SGX1234A', 1613545602
    vehicle_type, plate, billed = carpark1.vehicle_exit(plate, exit_time)
    assert vehicle_type == 'motorcycle'
    assert plate == 'SGX1234A'
    assert billed == 2