from hypothesis import given, strategies as st
from carparking_main import Carpark
import math
import sys

original_stdout = sys.stdout


@ given(st.integers(min_value=0, max_value=100000), st.integers(min_value=0, max_value=100000))
def lots_are_constant(car_lots, motorcycle_lots):
    carpark_attribute_map = [('car', car_lots, 2), ('motorcycle', motorcycle_lots, 1)]
    carpark = Carpark(carpark_attribute_map, fee_time_block=3600)
    assert len(carpark.lotsAvailability['car']) == car_lots \
           and len(carpark.lotsAvailability['motorcycle']) == motorcycle_lots


carpark_attribute_map = [('car', 100, 2)]
carpark1 = Carpark(carpark_attribute_map, fee_time_block=3600)


@ given(st.characters(), st.integers(min_value=0, max_value=100000))
def lots_never_exceeded(plate, time):
    carpark1.vehicle_entry('car', plate, time)
    assert sum(carpark1.lotsAvailability['car']) <= 100


@ given(st.characters(), st.integers(min_value=0, max_value=100000))
def reject_when_full(plate, time):
    carpark1.vehicle_entry('car', plate, time)
    assert sum(carpark1.lotsAvailability['car']) == 100


@ given(st.integers(min_value=0, max_value=1000000))
def rounding_to_nearest_hour(time_delta):
    blocks = carpark1.calculate_billable_blocks(time_delta)
    assert blocks == math.floor(time_delta/carpark1.FeeTimeBLock) + 1

if __name__ == '__main__':
    with open('temp.txt', 'w') as w:
        sys.std = w
        lots_are_constant()
        lots_never_exceeded()
        reject_when_full()
        rounding_to_nearest_hour()
