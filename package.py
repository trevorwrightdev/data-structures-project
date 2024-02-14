class Package:
    def __init__(self, id, delivery_address, deadline, city, zipcode, weight):
        self.id = id
        self.delivery_addres = delivery_address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = "AT THE HUB"
        self.delivery_time = None
        