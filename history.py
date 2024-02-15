from datetime import datetime

class History:
    def __init__(self):
        self.package_states = {}

    def save(self, time, package, new_state):
        if package not in self.package_states:
            self.package_states[package] = {
                "AT THE HUB": "8:00AM",
                "EN ROUTE": None,
                "DELIVERED": None
            }  
        self.package_states[package][new_state] = time

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