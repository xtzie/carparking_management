import argparse
import sys

#create a data class - for carpark options - read values in from config file
# read from config, env variables - override values, override by command line flags
#12 factor app 
#inputs and outputs are in the command line

class Carpark:
    def __init__(self, car_lots, motorcycle_lots, motorcycle_fee=1, car_fee=2, hour_conversion=3600):
        self.carLots = [0] * car_lots
        self.motorcycleLots = [0] * motorcycle_lots
        self.vehicleMap = {}
        self.motorcycleFee = motorcycle_fee
        self.carFee = car_fee
        self.hourConversion = hour_conversion
        #could lead to inconsistent state 
        # car object
        # motorcycle object
        # entry function
    def carEntry(self, plate, time_in):
        try:
            assigned = self.carLots.index(0)
            self.carLots[assigned] = 1
            self.vehicleMap[plate] = [assigned, time_in, 'CarLot']
            statement = f'Accept CarLot{assigned + 1}'
            print(statement)
        except:
            print('Reject')

    def motorcycleEntry(self, plate, time_in):
        try:
            assigned = self.motorcycleLots.index(0)
            self.motorcycleLots[assigned] = 1
            self.vehicleMap[plate] = [assigned, time_in, 'MotorcycleLot']
            statement = f'Accept MotorcycleLot{assigned + 1}'
            print(statement)
            
        except:
            print('Reject')

    def vehicleExit(self, plate, time_out):
        try:
            assigned, time_in, lot = self.vehicleMap.pop(plate)
        except:
            statement = f'ERROR: Vehicle {plate} does not exist!'
            print(statement)
            return
            
        
        time_delta = time_out - time_in
        
        if time_delta < 0:
            statement = f'ERROR: Vehicle {plate} exit time earlier than entry by {time_delta} seconds!'
            print(statement)
            return
            
        
        billable_time = (time_delta // self.hourConversion + (time_delta % self.hourConversion >= 0))
        
        if lot == 'MotorcycleLot':
            self.motorcycleLots[assigned] = 0
            billed = billable_time * self.motorcycleFee
        elif lot == 'CarLot':
            billed = billable_time * self.carFee
            self.carLots[assigned] = 0
        
        statement = f'{lot}{assigned + 1} {billed}'
        print(statement)


def BootstrapData(file_lines):
    #read first line
    data = file_lines.readline()
    #####################################################
    #Ensure first line inputs are integers
    try:
        data = ([int(x) for x in data.split()])
        
    except Exception as e:
        error_text = f'ERROR: First line input should state car parking and motorcycle parking lots in the format: int int \n \n{e}'
        print(error_text)
        sys.exit()
    
    carLots, bikeLots = data[0], data[1]
    
    #Ensure first line inputs non-negative integers
    if carLots < 0 or bikeLots < 0:
        print('ERROR: Please ensure that car parking and motorcycle parking lots are not negative numbers')
        sys.exit()
    #####################################################
    #Instantiate Carpark object
    carpark = Carpark(carLots, bikeLots)
    
    #Main loop for the input file
    for idx, entry in enumerate(file_lines):
        
        #split input text string by spaces
        input = [x for x in entry.split()]
        
        #Ensure input has sufficient variables
        num_variables = len(input)
        if num_variables < 3:
            print(f'line{idx+2} ERROR: Minimum 3 variables expected, received: {num_variables}')
            continue
        ######################Use their existing inputs - whether it is entering or exiting, if input is not well formed, throw back
        #Ensure input does not have excess variables
        if num_variables > 4:
            print(f'line{idx+2} ERROR: Maximum 4 variables expected, received: {num_variables}')
            continue
        
        #assign variables from input list
        vehicle_number = str(input[-2])
        
        #ensure that time is presented as integer
        ###########replace with time library
        try:
            time = int(input[-1])
            
        except:
            print(f'line{idx+2} ERROR: Time not in number format, received: {input[-1]}')
            continue
        
        #Vehicle entry
        if num_variables == 4 and input[0].lower() == 'enter':
            type = input[1].lower()
            if type == 'car':
                carpark.carEntry(vehicle_number, time)
            elif type == 'motorcycle':
                carpark.motorcycleEntry(vehicle_number, time)
            else:
                print(f'line{idx+2} ERROR: Vehicle type not correctly specified, received: {input[1]}')
        
        #Vehicle exit
        elif num_variables == 3 and input[0].lower() == 'exit':
            vehicle_number = input[1]
            carpark.vehicleExit(vehicle_number, time)
        
        else:
            print(f'line{idx+2} ERROR: Inconsistent input format.')



if __name__ == "__main__":
    file_parser = argparse.ArgumentParser()
    file_parser.add_argument('-file', metavar='', required = True, help='Input file of Car Parking Data')
    args = file_parser.parse_args()

    file_name = args.file
    with open(args.file) as file_lines:
        BootstrapData(file_lines)