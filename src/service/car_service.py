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



    def __in_order(self, e1, e2):
        pass

    def __merge_sort(self, car_list):
        if len(car_list) <= 1:
            return car_list

        m = len(car_list) // 2
        left = self.__merge_sort(car_list[:m])
        right = self.__merge_sort(car_list[m:])
        return self.merge(left, right)

    def merge(self, left, right):
        rez = []
        while len(left) > 0 and len(right) > 0:
            if self.__in_order(left[0], right[0]):
                rez.append(left.pop(0))
            else:
                rez.append(right.pop(0))
        rez.extend(left + right)
        return rez

