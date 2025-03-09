from tkinter.constants import RIGHT


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
        list=self.get_all_cars()
        for i in range (0,len(list)):
            for j in range (0,len(list)-1):
                if comparator=="tokenMasina":
                    if list[j].tokenMasina>list[j+1].tokenMasina:
                        aux=list[j]
                        list[j]=list[j+1]
                        list[j+1]=aux

                if comparator=="marca model":
                    if list[j].marca>list[j+1].marca:
                        aux=list[j]
                        list[j]=list[j+1]
                        list[j+1]=aux
                    if list[j].marca==list[j+1].marca:
                        if list[j].model > list[j + 1].model:
                            aux = list[j]
                            list[j] = list[j + 1]
                            list[j + 1] = aux

                if comparator=="marca model tokenMasina":
                    if list[j].marca>list[j+1].marca:
                        aux=list[j]
                        list[j]=list[j+1]
                        list[j+1]=aux
                    if list[j].marca==list[j+1].marca:
                        if list[j].model > list[j + 1].model:
                            aux = list[j]
                            list[j] = list[j + 1]
                            list[j + 1] = aux

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
        return False

    def quick_sort(self, car_list, comparator):
        if len(car_list) <= 1:
            return car_list

        p = [x for x in car_list if x == car_list[0]]
        left = [x for x in car_list if self.in_order_quick_sort(x, p[0], comparator)]
        right = [x for x in car_list if self.in_order_quick_sort(p[0], x, comparator)]

        return self.quick_sort(left, comparator) + p + self.quick_sort(right, comparator)












