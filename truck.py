import csv
from datetime import datetime, timedelta
from logs import colored_output

# This function reads the distances.csv file and returns the data as a 2d array of floats.
def get_distances_matrix():
    matrix = []
    with open('distances.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_float = [float(value) if value != '' else None for value in row]
            matrix.append(row_float)
    return matrix

# This function reads the addresses.csv file and returns the data as a dictionary with the address as the key and the index as the value.
# This is so we can use any given address to find distances in the distances_matrix.
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

# This function takes two addresses and returns the distance between them.
def get_distance_between(address1, address2):
    index1 = addresses[address1]
    index2 = addresses[address2]

    distance = distances_matrix[index1][index2]

    # If the distance is None, it means it was not found. in this case we should do the reverse because we know that it exists in the matrix. 
    if distance == None:
        distance = distances_matrix[index2][index1]

    return distance

class Truck:
    # The truck class is used to represent a truck that will deliver packages.
    def __init__(self, id):
        self.id = id
        self.loaded_packages = []
        self.current_location = "HUB"
        self.miles_driven = 0.0
        self.current_time = "08:00AM"
    
    # Loads a package onto the truck by adding it to the loaded_packages list. 
    def load(self, package, history):

        # cannot be loaded if the truck is full or if the truck is not at the hub
        if len(self.loaded_packages) == 16:
            raise Exception("Truck is full")
        if self.current_location != "HUB":
            raise Exception("Truck is not at the hub")

        self.loaded_packages.append(package)
        package.update_status("EN ROUTE")

        # saves the package state change to the history for queries later
        history.save(self.current_time, package, "EN ROUTE")
    
    def drive_to_location(self, location):
        # get distance between locations
        distance = get_distance_between(self.current_location, location)

        # update truck state
        self.current_location = location
        # update miles driven based on the distance traveled
        self.miles_driven += distance

        # pass the time
        self.current_time = self.get_new_time(distance)

        colored_output('bright_yellow', 'Truck ' + str(self.id) + ' drives '+ str(distance) + ' miles to ' + location + ' and arrives at ' + self.current_time)

    # Unloads all packages that are meant for the current location we are at
    def unload(self, history):
        packages_unloaded = []

        for package in self.loaded_packages:
            if package.delivery_address == self.current_location:
                package.update_status("DELIVERED")
                package.delivery_time = self.current_time
                packages_unloaded.append(package)
                colored_output('bright_green', 'Package ' + str(package.id) + ' has been delivered to ' + self.current_location + '!')

                # saves the package state change to the history for queries later
                history.save(self.current_time, package, "DELIVERED")
        
        # Remove unloaded packages from self.loaded_packages
        for package in packages_unloaded:
            self.loaded_packages.remove(package)
    
    # This function takes a distance and returns the new time after the truck has traveled that distance.
    def get_new_time(self, distance):
        # 18 miles per hour
        speed = 18

        time_taken = distance / speed
        current_time_obj = datetime.strptime(self.current_time, "%I:%M%p")
        new_time_obj = current_time_obj + timedelta(hours=time_taken)
        new_time_formatted = new_time_obj.strftime("%I:%M%p")
        return new_time_formatted
    
    # This function returns the nearest package to the truck's current location.
    def get_nearest_package(self):
        nearest_package = None
        nearest_distance = 100000
        for package in self.loaded_packages:
            distance = get_distance_between(self.current_location, package.delivery_address)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package
        return nearest_package
                
