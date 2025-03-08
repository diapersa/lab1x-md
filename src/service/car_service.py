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



