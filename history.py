from datetime import datetime
import copy

class History:

    # This class is used to keep track of the state of packages at different times.
    def __init__(self):
        self.package_states = {}

    # This function takes a time, a package, and a new state and saves the state change to the history.
    def save(self, time, package, new_state):
        if package not in self.package_states:
            self.package_states[package] = {
                "AT THE HUB": "7:59AM",
                "EN ROUTE": None,
                "DELIVERED": None,
            }  
        self.package_states[package][new_state] = time

    # returns a snapshot of all of the package states based on the time given
    def get_by_time(self, query_time):
        package_history = []
        query_time_dt = datetime.strptime(query_time, "%I:%M%p")

        earliest_time_dt = datetime.strptime("7:59AM", "%I:%M%p")
        if query_time_dt < earliest_time_dt:
            query_time_dt = earliest_time_dt

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

        