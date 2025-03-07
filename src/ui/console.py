
class ConsoleUI:
    def __init__(self, car_console):
        self.__car_console = car_console

    def __help(self, cmd):
        help_command = {
            'PRINT-ALL': "Usage: PRINT-ALL",
            'SEARCH': "Usage: SEARCH <tokenMasina>",
            'SORT': "Usage: SORT <tokenMasina>"
        }
        try:
            print(help_command[cmd])
        except KeyError:
            print(f"No help for command {cmd}")

    def __create_commands(self):
        return {
            "PRINT-ALL": self.__car_console.print_all_cars,
            "SEARCH": self.__car_console.search_cars,
            "SORT tokenMasina": self.__car_console.sort_cars,
            "SORT marca model": self.__car_console.sort_cars,
            "SORT marca model tokenMasina": self.__car_console.sort_cars,
            "SORT profit": self.__car_console.sort_cars,
            "help": self.__help,
        }

    def __print_commands(self, commands):
        print("\nChoose command: ", end="\n\t")
        print(*commands.keys(), "exit", sep=" --- ")
        print("For HELP write: help <command>. E.g: help SORT tokenMasina")

    def __read_commands(self):
        command = input("Command: ")
        pos = command.find(' ')

        if pos == -1:
            return command, []

        cmd = command[:pos]
        args = command[pos:]
        args = args.split(',')
        args = [s.strip() for s in args]
        return cmd, args

    def run_commands(self):
        commands = self.__create_commands()
        while True:
            self.__print_commands(commands)
            try:
                cmd, args = self.__read_commands()
            except ValueError:
                print("Invalid command")
                continue

            if cmd == "exit":
                break
            try:
                commands[cmd](*args)
            except KeyError:
                print(f"No command {cmd}")






