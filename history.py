import copy
from datetime import datetime

class History:
    def __init__(self, package_map):
        self.package_map = package_map
        self.data = {}

    def save(self, time):
        self.data[time] = copy.deepcopy(self.package_map)

    def get(self, query_time):
        query_time_dt = datetime.strptime(query_time, "%I:%M%p")
        
        closest_time = None
        closest_time_dt = None
        
        for stored_time in self.data.keys():
            stored_time_dt = datetime.strptime(stored_time, "%I:%M%p")
            
            if stored_time_dt <= query_time_dt:
                if closest_time is None or stored_time_dt > closest_time_dt:
                    closest_time = stored_time
                    closest_time_dt = stored_time_dt
        
        if closest_time is not None:
            return self.data[closest_time]
        else:
            return None