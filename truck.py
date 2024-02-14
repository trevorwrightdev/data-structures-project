import csv
from datetime import datetime, timedelta
from logs import print_line, colored_output

def get_distances_matrix():
    matrix = []
    with open('distances.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_float = [float(value) if value != '' else None for value in row]
            matrix.append(row_float)
    return matrix

def get_address_csv():
    addresses_dict = {}
    with open('addresses.csv', 'r') as file:
        addresses = file.readlines()
        for index, address in enumerate(addresses):
            address = address.strip()  
            addresses_dict[address] = index
    return addresses_dict

# 2d array of distances between addresses
distances_matrix = get_distances_matrix()
# map of addresses with address as key and index as value
addresses = get_address_csv()

def get_distance_between(address1, address2):
    index1 = addresses[address1]
    index2 = addresses[address2]

    distance = distances_matrix[index1][index2]
    if distance == None:
        distance = distances_matrix[index2][index1]

    return distance

class Truck:
    def __init__(self, id):
        self.id = id
        self.loaded_packages = set()
        self.current_location = "HUB"
        self.miles_driven = 0
        self.current_time = "08:00 AM"
    
    def load(self, package):
        if len(self.loaded_packages) == 16:
            raise Exception("Truck is full")
        if self.current_location != "HUB":
            raise Exception("Truck is not at the hub")

        self.loaded_packages.add(package)
        package.update_status("EN ROUTE")
    
    def drive_to_location(self, location):
        # get distance between locations
        distance = get_distance_between(self.current_location, location)

        self.current_location = location
        self.miles_driven += distance

        # pass the time
        self.current_time = self.get_new_time(distance)

    def unload(self):
        packages_unloaded = set()

        for package in self.loaded_packages:
            if package.delivery_address == self.current_location:
                package.update_status("DELIVERED")
                package.delivery_time = self.current_time
                packages_unloaded.add(package)
                colored_output('bright_green', 'Package ' + str(package.id) + ' delivered at ' + self.current_location + ' at ' + self.current_time)
        
        self.loaded_packages = self.loaded_packages - packages_unloaded
    
    def get_new_time(self, distance):
        speed = 18
        time_taken = distance / speed
        current_time_obj = datetime.strptime(self.current_time, "%I:%M %p")
        new_time_obj = current_time_obj + timedelta(hours=time_taken)
        new_time_formatted = new_time_obj.strftime("%I:%M %p")
        return new_time_formatted
    
    def get_nearest_package(self):
        nearest_package = None
        nearest_distance = 100000
        for package in self.loaded_packages:
            distance = get_distance_between(self.current_location, package.delivery_address)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package
        return nearest_package
                
