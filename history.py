from datetime import datetime
import copy

class History:
    def __init__(self):
        self.package_states = {}

    def save(self, time, package, new_state):
        if package not in self.package_states:
            self.package_states[package] = {
                "AT THE HUB": "7:59AM",
                "EN ROUTE": None,
                "DELIVERED": None,
            }  
        self.package_states[package][new_state] = time

    def get(self, query_time):
        package_history = []
        query_time_dt = datetime.strptime(query_time, "%I:%M%p")
        for package, states in self.package_states.items():
            latest_state = None
            latest_time_dt = None
            for state, time_str in states.items():
                if time_str:  
                    state_time_dt = datetime.strptime(time_str, "%I:%M%p")
                    if state_time_dt <= query_time_dt:
                        if latest_time_dt is None or state_time_dt > latest_time_dt:
                            latest_state = state
                            latest_time_dt = state_time_dt
            
            package_copy = copy.deepcopy(package)
            package_copy.status = latest_state
            package_history.append(package_copy)
        
        package_history_sorted = sorted(package_history, key=lambda package: package.id)

        return package_history_sorted

        