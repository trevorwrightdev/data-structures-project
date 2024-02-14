class Truck:
    def __init__(self):
        self.loaded_packages = set()
        self.current_location = "HUB"
        self.miles_driven = 0
        self.current_time = "8:00 AM"
    
    def load(self, package):
        if len(self.loaded_packages) == 16:
            raise Exception("Truck is full")

        self.loaded_packages.add(package)
        package.update_status("EN ROUTE")
    
    def drive_to_location(self, location, distance):
        self.current_location = location
        self.miles_driven += distance

        # pass the time
        self.current_time = self.get_new_time(distance)

        

    def unload(self):
        for package in self.loaded_packages:
            if package.delivery_address == self.current_location:
                package.update_status("DELIVERED")
                package.delivery_time = self.current_time
                self.loaded_packages.remove(package)
    
    def get_new_time(self, distance):
        # Calculate time taken to travel the distance
        time_taken_hours = distance / 18

        # Split current time into hours and minutes
        current_hour, current_minute = map(int, self.current_time[:-6].split(':'))
        am_pm = self.current_time[-2:]

        # Convert current time to minutes
        total_minutes = current_hour * 60 + current_minute

        # Add time taken to current time
        total_minutes += time_taken_hours * 60

        # Calculate new hours and minutes
        new_hour = total_minutes // 60
        new_minute = total_minutes % 60

        # Format new time
        new_time = f"{new_hour % 12 or 12}:{new_minute:02d} {am_pm}"

        return new_time
                
