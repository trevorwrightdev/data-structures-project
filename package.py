from logs import colored_output

class Package:

    # This class simply stores package data 
    def __init__(self, id, delivery_address, deadline, city, zipcode, weight):
        self.id = id
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = "AT THE HUB"
        self.delivery_time = None
    
    # This function updates the status of the package
    def update_status(self, status):
        self.status = status

    # This function prints the package data with nice color formatting
    def print(self):
        output_string = "ID: " + str(self.id) + ", Address: " + self.delivery_address + ", Deadline: " + self.deadline + ", City: " + self.city + ", Zipcode: " + str(self.zipcode) + ", Weight: " + str(self.weight) + ", Status: " + self.status

        if self.status == "DELIVERED":
            output_string += ", Delivery Time: " + str(self.delivery_time)
            color = 'green'
        elif self.status == "EN ROUTE":
            color = 'yellow'
        else:
            color = 'red'

        colored_output(color, output_string)
