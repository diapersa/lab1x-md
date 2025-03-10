from tkinter.constants import RIGHT

from src.domain.car import Car
import time

class CarService:
    def __init__(self, car_repository):
        self.__car_repository = car_repository

    def get_all_cars(self):
        return self.__car_repository.get_all_cars()

    def linear_search_car_by_token(self, car_token):
        for car in self.get_all_cars():
            if car.tokenMasina==car_token:
                return car

    def compare_bubble_sort(self, car1, car2, comparator):
        if comparator == "tokenMasina":
            if car1.tokenMasina > car2.tokenMasina:
                car1,car2= car2, car1

        if comparator == "marca model":
            if car1.marca > car2.marca:
                car1,car2= car2, car1
            if car1.marca == car2.marca:
                if car1.model > car2.model:
                    car1,car2= car2, car1

        if comparator == "marca model tokenMasina":
            if car1.marca > car2.marca:
                car1,car2= car2, car1
            if car1.marca == car2.marca:
                if car1.model > car2.model:
                    car1,car2= car2, car1
                if car1.model == car2.model:
                    if car1.tokenMasina == car2.tokenMasina:
                        car1,car2= car2, car1

        if comparator == "profit":
            if car1.profit > car2.profit:
                car1, car2= car2, car1
        return car1, car2

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
                pass
            #TODO model
        return -2

    def compare_marca_model_tokenMasina(self, car1, car2):
        if car1.marca > car2.marca:
            return 2
        else:
            if car1.marca == car2.marca:
                pass
            #TODO model+tokenMasina
        return -2



    def bubble_sort(self, comparator):
        list=self.get_all_cars()
        for i in range (0,len(list)):
            for j in range (0,len(list)-1):
                if comparator(list[j], list[j+1])>1:
                    list[j], list[j+1]=list[j+1], list[j]
        for car in list:
            print(car)



        return self.get_all_cars()










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

    def in_order_quick_sort(self, car1, car2, comparator):
        if comparator == "tokenMasina":
            return car1.tokenMasina < car2.tokenMasina
        elif comparator == "marca model":
            return (car1.marca, car1.model) < (car2.marca, car2.model)
        elif comparator == "marca model tokenMasina":
            return (car1.marca, car1.model, car1.tokenMasina) < (car2.marca, car2.model, car2.tokenMasina)
        elif comparator == "profit":
            return Car.profit(car1) < Car.profit(car2)
        return False

    def quick_sort(self, car_list, comparator):
        if len(car_list) <= 1:
            return car_list

        p = [x for x in car_list if x == car_list[0]]
        left = [x for x in car_list if self.in_order_quick_sort(x, p[0], comparator)]
        right = [x for x in car_list if self.in_order_quick_sort(p[0], x, comparator)]

        return self.quick_sort(left, comparator) + p + self.quick_sort(right, comparator)


    ###












