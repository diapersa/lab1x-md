class CarService:
    def __init__(self, car_repository):
        self.__car_repository = car_repository

    def get_all_cars(self):
        return self.__car_repository.get_all_cars()

    def search_car_by_token(self, car_token):
        pass

