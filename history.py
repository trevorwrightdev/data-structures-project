import copy

class History:
    def __init__(self, package_map):
        self.package_map = package_map
        self.data = {}

    def save(self, time):
        self.data[time] = copy.deepcopy(self.package_map)