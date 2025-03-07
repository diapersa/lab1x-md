class CarConsole:
    def __init__(self, car_service):
        self.__car_service = car_service

    def print_all_cars(self):
        car_list = self.__car_service.get_all_cars()
        for car in car_list:
            print(car)

    def search_cars(self):
        pass

    def sort_cars(self):
        pass