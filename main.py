from hashmap import HashMap
from package import Package
from truck import Truck
from logs import print_line, colored_output
import csv

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

def load_truck(truck, packages):
    print_line()
    colored_output('blue', 'TRUCK ' + str(truck.id) + ' LOADING PHASE')
    for package in packages:
        colored_output('cyan', 'Loading package ' + str(package.id) + ' into truck ' + str(truck.id) + '...')
        truck.load(package)
    print_line()

def delivery_algorithm(truck):
    print_line()
    colored_output('green', 'TRUCK ' + str(truck.id) + ' DELIVERY PHASE')

    # loop continues until the truck has no more packages
    while (len(truck.loaded_packages) > 0):
        nearest_package = truck.get_nearest_package()
        truck.drive_to_location(nearest_package.delivery_address)
        truck.unload()
    
    truck.drive_to_location("HUB")
    colored_output('red', 'Total miles driven by truck ' + str(truck.id) + ': ' + str(truck.miles_driven) + ' miles')
    print_line()
        
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
    
    # * Algorithm
    # map of packages with package id as key and package object as value
    packages = get_package_map()
    truck1 = Truck(1)
    truck2 = Truck(2)

    # Loading phase 
    load_truck(truck1, [
        packages.get(1),
        packages.get(13),
        packages.get(14),
        packages.get(15),
        packages.get(16),
        packages.get(20),
        packages.get(21),
        packages.get(29),
        packages.get(30),
        packages.get(31),
        packages.get(33),
        packages.get(34),
        packages.get(35),
        packages.get(37),
        packages.get(39),
        packages.get(40)
    ])
    load_truck(truck2, [   
        packages.get(2),
        packages.get(3),
        packages.get(4),
        packages.get(5),
        packages.get(7),
        packages.get(8),
        packages.get(10),
        packages.get(11),
    ])

    # Delivery phase
    delivery_algorithm(truck1)
    delivery_algorithm(truck2)

    pass

main()