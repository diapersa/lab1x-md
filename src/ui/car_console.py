class CarConsole:
    def __init__(self, car_service):
        self.__car_service = car_service

    def get_all_cars(self):
        return self.__car_service.get_all_cars()

    def print_all_cars(self):
        car_list = self.get_all_cars()
        for car in car_list:
            print(car)

    def search_car_by_token(self, car_token):
        car_list = self.get_all_cars()

        ## linear search
        # self.__car_service.search_car_by_token(car_token)

        ## binary search
        ## for this method, the car list MUST BE SORTED by the token in this case

        sorted_car_list = self.__car_service.quick_sort(car_list, "tokenMasina")
        self.__print_cars(sorted_car_list)
        pos_found_car = self.__car_service.binary_search_car_by_token(sorted_car_list, car_token, 0, len(sorted_car_list) - 1)
        if pos_found_car != -1:
            print("The car is found! ", sorted_car_list[pos_found_car])
        else:
            print("The car was not found!")

    def __print_cars(self, car_list):
        for car in car_list:
            print(car)

    def sort_cars(self, comparator):
        car_list = self.get_all_cars()

        ## bubble sort
        # self.__car_service.bubble_sort(comparator)
        # self.print_all_cars()

        ## quick sort
        quick_sorted_car_list = self.__car_service.quick_sort(car_list, comparator)
        self.__print_cars(quick_sorted_car_list)
