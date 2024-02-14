import csv
from datetime import datetime, timedelta

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
    def __init__(self):
        self.loaded_packages = set()
        self.current_location = "HUB"
        self.miles_driven = 0
        self.current_time = "08:00 AM"
    
    def load(self, package):
        if len(self.loaded_packages) == 16:
            raise Exception("Truck is full")

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
        for package in self.loaded_packages:
            if package.delivery_address == self.current_location:
                package.update_status("DELIVERED")
                package.delivery_time = self.current_time
                self.loaded_packages.remove(package)
    
    def get_new_time(self, distance):
        # Speed is 18 miles per hour
        speed = 18
        # Calculate time taken to cover the distance in hours
        time_taken = distance / speed

        # Convert current time to datetime object
        current_time_obj = datetime.strptime(self.current_time, "%I:%M %p")

        # Calculate new time by adding the duration
        new_time_obj = current_time_obj + timedelta(hours=time_taken)

        # Convert back to the required format
        new_time_formatted = new_time_obj.strftime("%I:%M %p")

        return new_time_formatted
                
