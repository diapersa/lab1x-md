class CarRepository:
    def __init__(self):
        self.__car_list = []

    def add_car(self, car):
        self.__car_list.append(car)

    def get_all_cars(self):
        return self.__car_list