# import time
#
#
# class CarConsole:
#     def __init__(self, car_service):
#         self.__car_service = car_service
#
#     def get_all_cars(self):
#         return self.__car_service.get_all_cars()
#
#     def print_all_cars(self):
#         car_list = self.get_all_cars()
#         for car in car_list:
#             print(car)
#
#     def search_car_by_token(self, car_token):
#         car_list = self.get_all_cars()
#
#         ###### linear search
#         start_time1 = time.perf_counter()
#         print(self.__car_service.linear_search_car_by_token(car_token))
#         end_time1 = time.perf_counter()
#
#
#
#         # ## binary search and execution time
#         # ## for this method, the car list MUST BE SORTED by the token in this case
#         #
#         # sorted_car_list = self.__car_service.quick_sort(car_list, "tokenMasina")
#         # self.__print_cars(sorted_car_list)
#         #
#         # ### time.perf_counter() is more precise than time.time() !!!!!!!!!!!
#         # start_time2 = time.perf_counter()
#         # pos_found_car = self.__car_service.binary_search_car_by_token(sorted_car_list, car_token, 0, len(sorted_car_list) - 1)
#         # end_time2 = time.perf_counter()
#         #
#         # if pos_found_car != -1:
#         #     print("The car is found! ", sorted_car_list[pos_found_car])
#         # else:
#         #     print("The car was not found!")
#         # print(f"\nThe execution time for binary search is: {end_time2 - start_time2:.9f} seconds")
#
#         print(f"\nThe execution time for linear search is: {end_time1 - start_time1:.9f} seconds")
#
#     def __print_cars(self, car_list):
#         for car in car_list:
#             print(car)
#
#     def bubble_sort(self, comparator):
#         for car in self.__car_service.bubble_sort(comparator):
#             print (car)
#
#     def sort_cars(self, comparator):
#         car_list = self.get_all_cars()
#
#         ######## bubble sort and execution time
#         self.__car_service.bubble_sort(comparator)
#
#         start_time1=time.perf_counter()
#         bubble_sorted_car_list=self.__car_service.bubble_sort(comparator)
#         end_time1=time.perf_counter()
#         self.__print_cars(bubble_sorted_car_list)
#
#         print(f"\nThe execution time for bubble sort is: {end_time1 - start_time1:.9f} seconds")
#
#
#         # ######## quick sort and execution time
#         # ### time.perf_counter() is more precise than time.time() !!!!!!!!!!!
#         # start_time2 = time.perf_counter()
#         # quick_sorted_car_list = self.__car_service.quick_sort(car_list, comparator)
#         # end_time2 = time.perf_counter()
#         # self.__print_cars(quick_sorted_car_list)
#
#         # {end_time2 - start_time2:.9f}
#         # .9 for zecimale dupa virgula and f for floating-point (zecimal)
#         # print(f"\nThe execution time for quick sort is: {end_time2 - start_time2:.9f} seconds")
