from hypothesis import given, strategies as st
from carparking_main import Carpark


@ given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x + 1

@ given(st.integers(), st.integers())
def lots_are_constant(car_lots, motorcycle_lots):
    carpark = Carpark(car_lots, motorcycle_lots)
    assert len(car_lots) == carpark.carLots and len(motorcycle_lots) == carpark.motorcycleLots

@ given(st.integers(), st.integers())
def lots_never_exceeded()

if __name__ == '__main__':
    lots_are_constant()
