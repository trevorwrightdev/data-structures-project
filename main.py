from hashmap import HashMap
from package import Package
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

def get_address_csv():
    addresses_dict = {}
    with open('addresses.csv', 'r') as file:
        addresses = file.readlines()
        for index, address in enumerate(addresses):
            address = address.strip()  
            addresses_dict[address] = index
    return addresses_dict

def get_distances_matrix():
    matrix = []
    with open('distances.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_float = [float(value) if value != '' else None for value in row]
            matrix.append(row_float)
    return matrix

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
        notes = package['notes']
        new_package = Package(package_id, delivery_address, deadline, city, zipcode, weight)
        map.insert(package_id, new_package)
    return map

# map of packages with package id as key and package object as value
packages = get_package_map()
# map of addresses with address as key and index as value
addresses = get_address_csv()
# 2d array of distances between addresses
distances_matrix = get_distances_matrix()

def get_distance_between(address1, address2):
    index1 = addresses[address1]
    index2 = addresses[address2]

    distance = distances_matrix[index1][index2]
    if distance == None:
        distance = distances_matrix[index2][index1]

    return distance

def main():
    print('\n')
    colored_output('cyan', 'Welcome to the WGUPS package delivery system! What would you like to do?')
    print('\n')
    colored_output('green', 's - Begin Package Delivery Simulation and Package Lookup')
    colored_output('green', 'q - Quit')
    print('\n')
    pass

main()