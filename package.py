class Package:
    def __init__(self, id, delivery_address, deadline, city, zipcode, weight):
        self.id = id
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = "AT THE HUB"
        self.delivery_time = None
    
    def update_status(self, status):
        self.status = status