import time



class CarConsole:
    def __init__(self, car_service):
        self.__car_service = car_service

    def get_all_cars(self):
        return self.__car_service.get_all_cars()

    def search_car_by_token(self, car_token):
        car_list = self.get_all_cars()

        # ###### linear search
        # start_time1 = time.perf_counter()
        # car = self.__car_service.linear_search_car_by_token(car_token)
        # print(car)
        # end_time1 = time.perf_counter()
        #
        # print(f"\nThe execution time for linear search is: {end_time1 - start_time1:.9f} seconds")


        ## binary search and execution time
        ## for this method, the car list MUST BE SORTED by the token in this case

        sorted_car_list = self.__car_service.quick_sort(car_list, "tokenMasina")
        self.__print_cars(sorted_car_list)

        ### time.perf_counter() is more precise than time.time() !!!!!!!!!!!
        start_time2 = time.perf_counter()
        pos_found_car = self.__car_service.binary_search_car_by_token(sorted_car_list, car_token, 0, len(sorted_car_list) - 1)
        end_time2 = time.perf_counter()

        if pos_found_car != -1:
            print("The car is found! ", sorted_car_list[pos_found_car])
        else:
            print("The car was not found!")
        print(f"\nThe execution time for binary search is: {end_time2 - start_time2:.9f} seconds")



    def __print_cars(self, car_list):
        for car in car_list:
            print(car)


    def sort_cars(self, comparator):
        car_list = self.get_all_cars()

        ######## bubble sort and execution time
        self.__car_service.bubble_sort(comparator)

        start_time1 = time.perf_counter()
        bubble_sorted_car_list = self.__car_service.bubble_sort(comparator)
        end_time1 = time.perf_counter()
        self.__print_cars(bubble_sorted_car_list)

        print(f"\nThe execution time for bubble sort is: {end_time1 - start_time1:.9f} seconds")

        # ######## quick sort and execution time
        # ### time.perf_counter() is more precise than time.time() !!!!!!!!!!!
        # start_time2 = time.perf_counter()
        # quick_sorted_car_list = self.__car_service.quick_sort(car_list, comparator)
        # end_time2 = time.perf_counter()
        # self.__print_cars(quick_sorted_car_list)

        # {end_time2 - start_time2:.9f}
        # .9 for zecimale dupa virgula and f for floating-point (zecimal)
        # print(f"\nThe execution time for quick sort is: {end_time2 - start_time2:.9f} seconds")




    def __help(self, cmd):
        help_command = {
            'PRINT-ALL': "Usage: PRINT-ALL",
            'SEARCH': "Usage: SEARCH <tokenMasina>",
            'SORT': "Usage: SORT <tokenMasina>, SORT <marca model>, SORT <marca model tokenMasina>, SORT <profit>"
        }
        try:
            print(help_command[cmd])
        except KeyError:
            print(f"No help for command {cmd}")


    def __options(self):
        print("\nPRINT-ALL-- SEARCH-- SORT tokenMasina-- SORT marca model-- SORT marca model tokenMasina-- SORT profit-- help(vom vedea)"

        )

    def run_commands(self):
        car_list = self.get_all_cars()
        self.__options()
        cmd = input("\nChoose an option: ")
        while cmd!="exit":
            match cmd:
                case "PRINT-ALL":
                    return self.__print_cars(self.get_all_cars())
                case "SEARCH":
                    car_token = input("Enter a token: ")
                    self.search_car_by_token(car_token)
                case "SORT tokenMasina":

                    start_time1 = time.perf_counter()
                    sorted_car_list= self.__car_service.bubble_sort(self.__car_service.compare_tokenMasina)
                    # sorted_car_list = self.__car_service.quick_sort(car_list, self.__car_service.compare_tokenMasina)
                    end_time1 = time.perf_counter()
                    self.__print_cars(sorted_car_list)

                    print(f"\nThe execution time is: {end_time1 - start_time1:.9f} seconds")


                case "SORT marca model":

                    start_time1 = time.perf_counter()
                    sorted_car_list = self.__car_service.bubble_sort(self.__car_service.compare_marca_model)
                    # sorted_car_list = self.__car_service.quick_sort(car_list, self.__car_service.compare_marca_model)
                    end_time1 = time.perf_counter()
                    self.__print_cars(sorted_car_list)

                    print(f"\nThe execution time is: {end_time1 - start_time1:.9f} seconds")


                case "SORT marca model tokenMasina":

                    start_time1 = time.perf_counter()
                    sorted_car_list = self.__car_service.bubble_sort(self.__car_service.compare_marca_model_tokenMasina)
                    # sorted_car_list = self.__car_service.quick_sort(car_list, self.__car_service.compare_marca_model_tokenMasina)
                    end_time1 = time.perf_counter()
                    self.__print_cars(sorted_car_list)

                    print(f"\nThe execution time is: {end_time1 - start_time1:.9f} seconds")

                case "SORT profit":

                    start_time1 = time.perf_counter()
                    sorted_car_list = self.__car_service.bubble_sort(self.__car_service.compare_profit)
                    # sorted_car_list = self.__car_service.quick_sort(car_list, self.__car_service.compare_profit)
                    end_time1 = time.perf_counter()
                    self.__print_cars(sorted_car_list)

                    print(f"\nThe execution time is: {end_time1 - start_time1:.9f} seconds")

                case "exit":
                    return "bye"
            self.__options()
            cmd = input("Choose an option: ")






    # def __help(self, cmd):
    #     help_command = {
    #         'PRINT-ALL': "Usage: PRINT-ALL",
    #         'SEARCH': "Usage: SEARCH <tokenMasina>",
    #         'SORT': "Usage: SORT <tokenMasina>, SORT <marca model>, SORT <marca model tokenMasina>, SORT <profit>"
    #     }
    #     try:
    #         print(help_command[cmd])
    #     except KeyError:
    #         print(f"No help for command {cmd}")
    #
    # def __create_commands(self):
    #     return {
    #         "PRINT-ALL": self.print_all_cars,
    #         "SEARCH": self.search_car_by_token,
    #         "SORT-tokenMasina": self.bubble_sort_tokenMasina,
    #         # "SORT marca model": self.__car_console.sort_cars,
    #         # "SORT marca model tokenMasina": self.__car_console.sort_cars,
    #         # "SORT profit": self.__car_console.sort_cars,
    #         "help": self.__help,
    #     }
    #
    # def __print_commands(self, commands):
    #     print("\nChoose command: ", end="\n\t")
    #     print(*commands.keys(), "exit", sep=" --- ")
    #     print("For HELP write: help <command>. E.g: help SORT tokenMasina/ marca model/ marca model tokenMasina/ profit")
    #
    # def __read_commands(self):
    #     command = input("Command: ")
    #     pos = command.find(' ')
    #
    #     if pos == -1:
    #         return command, []
    #
    #     cmd = command[:pos]
    #     args = command[pos:]
    #     args = args.split(',')
    #     args = [s.strip() for s in args]
    #     return cmd, args
    #
    #
    # def run_commands(self):
    #     commands = self.__create_commands()
    #     while True:
    #         self.__print_commands(commands)
    #         try:
    #             cmd, args = self.__read_commands()
    #
    #         except ValueError:
    #             print("Invalid command")
    #             continue
    #
    #         if cmd == "exit":
    #             break
    #         try:
    #             commands[cmd](*args)
    #
    #         except KeyError:
    #             print(f"No command {cmd}")







