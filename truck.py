class Truck:
    def __init__(self):
        self.loaded_packages = set()
        self.current_location = "HUB"
    
    def load_package(self, package_id):
        self.loaded_packages.add(package_id)