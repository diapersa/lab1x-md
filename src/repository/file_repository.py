from src.domain.car import Car
from src.repository.car_repository import CarRepository


class FileRepository(CarRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                line = line.strip()
                array = line.split(' ')
                new_car = Car(array[0], array[1], array[2], int(array[3]), int(array[4]))
                super().add_car(new_car)