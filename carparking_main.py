import argparse
import sys


class Carpark:
    def __init__(self, carpark_attribute_map, fee_time_block):
        self.lotsAvailability = {}
        self.feeMap = {}
        self.vehicleMap = {}

        # Measured in seconds. E.g 3600: hourly billing
        self.FeeTimeBLock = fee_time_block

        for details in carpark_attribute_map:
            vehicle_type, lots, fees = details
            assert lots >= 0, "Number of vehicle lots cannot be negative"
            assert fees >= 0, "Fees cannot be negative"
            self.lotsAvailability[vehicle_type] = [0] * lots
            self.feeMap[vehicle_type] = fees

    def vehicle_entry(self, vehicle_type, plate, time_in):
        try:
            vehicle_availability = self.lotsAvailability[vehicle_type]
        except Exception as e:
            print(f'Rejected entry for {plate}. Carpark does not allow for this vehicle type: {vehicle_type}')
            return
        try:
            assigned_idx = vehicle_availability.index(0)
        except:
            print('Reject')
            return

        vehicle_availability[assigned_idx] = 1
        self.vehicleMap[plate] = [assigned_idx, time_in, vehicle_type]
        statement = f'Accept {vehicle_type.capitalize()}Lot{assigned_idx + 1}'
        print(statement)

    def vehicle_exit(self, plate, time_out):
        try:
            assigned_lot, time_in, vehicle_type = self.vehicleMap.pop(plate)
        except:
            print(f'Rejected exit. Vehicle {plate} does not exist!')
            return

        time_delta = time_out - time_in

        if time_delta < 0:
            print(f'Rejected exit. Vehicle {plate} exit time of {time_out} earlier than entry time of {time_in}.')
            return

        billable_time = (time_delta // self.FeeTimeBLock + (time_delta % self.FeeTimeBLock >= 0))
        billed = self.feeMap[vehicle_type] * billable_time
        self.lotsAvailability[vehicle_type][assigned_lot] = 0

        statement = f'{vehicle_type.capitalize()}Lot{assigned_lot + 1} {billed}'
        print(statement)


def bootstrap_data(file_lines):
    # Instantiate carpark and validate first line inputs
    data = file_lines.readline()
    try:
        data = ([int(x) for x in data.split()])
    except:
        error_text = f'ERROR: First line input should state car parking and motorcycle parking lots.' \
                     f' Format should be: int int'
        print(error_text)
        sys.exit()

    car_lots, motorcycle_lots = data[0], data[1]
    if car_lots < 0 or motorcycle_lots < 0:
        print('ERROR: Please ensure that car parking and motorcycle parking lots are not negative numbers')
        sys.exit()

    # Instantiate carpark object
    carpark_attribute_map = [('car', car_lots, 2), ('motorcycle', motorcycle_lots, 1)]
    carpark = Carpark(carpark_attribute_map, 3600)

    # Main loop for the input file
    for idx, entry in enumerate(file_lines):

        input_data = [x for x in entry.split()]
        num_variables = len(input_data)

        if num_variables < 3:
            print(f'line{idx + 2} ERROR: Minimum 3 variables expected, received: {num_variables}')
            continue
        if num_variables > 4:
            print(f'line{idx + 2} ERROR: Maximum 4 variables expected, received: {num_variables}')
            continue

        # assign variables from input list
        vehicle_number = str(input_data[-2])

        # ensure that time is presented as integer
        try:
            time = int(input_data[-1])
        except:
            print(f'line{idx + 2} ERROR: Time not in number format, received: {input_data[-1]}')
            continue

        # Vehicle entry
        if num_variables == 4 and input_data[0].lower() == 'enter':
            type_ = input_data[1].lower()
            carpark.vehicle_entry(type_, vehicle_number, time)

        # Vehicle exit
        elif num_variables == 3 and input_data[0].lower() == 'exit':
            vehicle_number = input_data[1]
            carpark.vehicle_exit(vehicle_number, time)

        else:
            print(f'line{idx + 2} ERROR: Not able to process inputs. received:{input_data}')


if __name__ == "__main__":
    file_parser = argparse.ArgumentParser()
    file_parser.add_argument('-file', metavar='', required=True, help='Input file of Car Parking Data')
    args = file_parser.parse_args()

    file_name = args.file
    with open(args.file) as file_input:
        bootstrap_data(file_input)
