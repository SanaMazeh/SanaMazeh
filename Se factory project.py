class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

    def __str__(self):
        return f"{self.worker_id}, {self.name}, {self.start_city}"


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        return self.name


class WeDeliverSystem:
    def __init__(self):
        self.drivers = []
        self.cities = {}
        self.driver_id_counter = 1

    def generate_driver_id(self):
        return f"ID{self.driver_id_counter:03d}"

    def add_driver(self, name, start_city):
        if start_city not in self.cities:
            add_city = input(f"City {start_city} not found. Do you want to add it to the database? (yes/no): ")
            if add_city.lower() == "yes":
                self.add_city(start_city)
            else:
                print("Driver not added.")
                return
        driver_id = self.generate_driver_id()
        driver = Driver(driver_id, name, start_city)
        self.drivers.append(driver)
        self.driver_id_counter += 1
        print("Driver added successfully.")

    def add_city(self, city_name):
        if city_name not in self.cities:
            self.cities[city_name] = City(city_name)
            print(f"City {city_name} added to the database.")
        else:
            print(f"City {city_name} already exists.")

    def add_city_neighbor(self, city_name, neighbor_name):
        if city_name in self.cities and neighbor_name in self.cities:
            self.cities[city_name].add_neighbor(self.cities[neighbor_name])
        else:
            print("One or both cities do not exist.")

    def view_all_drivers(self):
        for driver in self.drivers:
            print(driver)

    def show_cities(self):
        for city in self.cities.values():
            print(city)

    def print_neighboring_cities(self, city_name):
        if city_name in self.cities:
            city = self.cities[city_name]
            for neighbor in city.neighbors:
                print(neighbor)
        else:
            print(f"City {city_name} not found.")

    def bfs_drivers_delivering_to_city(self, city_name):
        if city_name not in self.cities:
            print(f"City {city_name} not found.")
            return
        reachable_cities = self.bfs(city_name)
        for driver in self.drivers:
            if driver.start_city in reachable_cities:
                print(driver)

    def bfs(self, start_city):
        visited = set()
        queue = [start_city]
        reachable_cities = set()

        while queue:
            current_city = queue.pop(0)
            if current_city not in visited:
                visited.add(current_city)
                reachable_cities.add(current_city)
                for neighbor in self.cities[current_city].neighbors:
                    if neighbor.name not in visited:
                        queue.append(neighbor.name)

        return reachable_cities

    def main_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. To go to the drivers’ menu")
            print("2. To go to the cities’ menu")
            print("3. To exit the system")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.drivers_menu()
            elif choice == "2":
                self.cities_menu()
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def drivers_menu(self):
        while True:
            print("Enter:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. To go back to main menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_all_drivers()
            elif choice == "2":
                name = input("Enter the name of the driver: ")
                start_city = input("Enter the start city of the driver: ")
                self.add_driver(name, start_city)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def cities_menu(self):
        while True:
            print("Enter:")
            print("1. Show cities")
            print("2. Print neighboring cities")
            print("3. Print drivers delivering to city")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_cities()
            elif choice == "2":
                city_name = input("Enter the city name: ")
                self.print_neighboring_cities(city_name)
            elif choice == "3":
                city_name = input("Enter the city name: ")
                self.bfs_drivers_delivering_to_city(city_name)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = WeDeliverSystem()
    system.main_menu()
