class CarService:
    def __init__(self, car_repository):
        self.__car_repository = car_repository

    def get_all_cars(self):
        return self.__car_repository.get_all_cars()

    def search_car_by_token(self, car_token):
        for car in self.get_all_cars():
            if car.tokenMasina==car_token:
                print (car)

    def bubble_sort(self, comparator):
        for car1 in self.get_all_cars():
            for car2 in self.get_all_cars():
                if comparator=="tokenMasina":
                    if car1.tokenMasina<car2.tokenMasina:
                        aux=car1
                        car1=car2
                        car2=aux




