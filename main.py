from hashmap import HashMap
from package import Package
from truck import Truck
import csv

def colored_output(color, message):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'black': '\033[90m',
        'bright_red': '\033[91;1m',
        'bright_green': '\033[92;1m',
        'bright_yellow': '\033[93;1m',
        'bright_blue': '\033[94;1m',
        'bright_magenta': '\033[95;1m',
        'bright_cyan': '\033[96;1m',
        'bright_white': '\033[97;1m',
        'reset': '\033[0m'  
    }
    
    if color in colors:
        print(colors[color] + message + colors['reset'])
    else:
        print("Invalid color specified.")

def get_package_csv():
    data = []
    with open('packages.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_package_map():
    package_csv_data = get_package_csv()
    # Initializing the hashmap with 40 elements, one for each package. 
    map = HashMap(40)

    for package in package_csv_data:
        package_id = int(package['id'])
        delivery_address = package['delivery_address']
        deadline = package['deadline']
        city = package['city']
        zipcode = int(package['zip'])
        weight = int(package['weight'])
        new_package = Package(package_id, delivery_address, deadline, city, zipcode, weight)
        map.insert(package_id, new_package)
    return map



def main():
    print('\n')
    colored_output('cyan', 'Welcome to the WGUPS package delivery system! What would you like to do?')
    print('\n')
    colored_output('green', 's - Begin Package Delivery Simulation and Package Lookup')
    colored_output('green', 'q - Quit')
    print('\n')

    user_input = input('>')

    if user_input != 's':
        return
    
    # Algorithm

    # map of packages with package id as key and package object as value
    packages = get_package_map()
    truck = Truck()

    truck.load(packages.get(13))

    truck.drive_to_location("1060 Dalton Ave S")

    pass

main()