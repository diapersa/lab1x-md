from tkinter.constants import RIGHT

from src.domain.car import Car
import time

class CarService:
    def __init__(self, car_repository):
        self.__car_repository = car_repository

    def get_all_cars(self):
        return self.__car_repository.get_all_cars()

    def linear_search_car_by_token(self, car_token):
        car_list = self.get_all_cars()
        for car in car_list:
            if car.tokenMasina==car_token:
                return car

    def compare_tokenMasina(self, car1, car2):
        if car1.tokenMasina > car2.tokenMasina:
            return 2
        else:
            if car1.tokenMasina == car2.tokenMasina:
                return 0
        return -2

    def compare_marca_model(self, car1, car2):
        if car1.marca > car2.marca:
            return 2
        else:
            if car1.marca == car2.marca:
                if car1.model > car2.model:
                    return 2
                else:
                    if car1.model == car2.model:
                        return 0
        return -2


    def compare_marca_model_tokenMasina(self, car1, car2):
        if car1.marca > car2.marca:
            return 2
        else:
            if car1.marca == car2.marca:
                if car1.model > car2.model:
                    return 2
                else:
                    if car1.model == car2.model:
                        if car1.tokenMasina > car2.tokenMasina:
                            return 2
                        else:
                            if car1.tokenMasina == car2.tokenMasina:
                                return 0
        return -2


    def compare_profit(self, car1, car2):
        profit_car1 = Car.profit(car1)
        profit_car2 = Car.profit(car2)
        if profit_car1 > profit_car2:
            return 2
        else:
            if profit_car1 == profit_car2:
                return 0
        return -2

    def bubble_sort(self, comparator):
        list=self.get_all_cars()
        for i in range (0,len(list)):
            for j in range (0,len(list)-1):
                if comparator(list[j], list[j+1])>1:
                    list[j], list[j+1]=list[j+1], list[j]
        return list



    def binary_search_car_by_token(self, car_list, car_token, left, right):
        while left <= right:
            m = (left + right) // 2
            if car_token == car_list[m].tokenMasina:
                return m
            else:
                if car_token < car_list[m].tokenMasina:
                    right = m - 1
                else:
                    left = m + 1
        return -1


    def quick_sort(self, car_list, comparator):
        if len(car_list) <= 1:
            return car_list

        p = [x for x in car_list if x == car_list[0]]
        left = [x for x in car_list if comparator(x, p[0]) == -2]
        right = [x for x in car_list if comparator(p[0], x) == -2]

        return self.quick_sort(left, comparator) + p + self.quick_sort(right, comparator)


