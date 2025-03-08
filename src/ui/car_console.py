class CarConsole:
    def __init__(self, car_service):
        self.__car_service = car_service

    def print_all_cars(self):
        car_list = self.__car_service.get_all_cars()
        for car in car_list:
            print(car)

    def search_car_by_token(self, car_token):
        self.__car_service.search_car_by_token(car_token)


    def sort_cars(self, comparator):
        self.__car_service.bubble_sort(comparator)
        self.print_all_cars()