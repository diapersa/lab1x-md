from src.repository.car_repository import CarRepository
from src.repository.file_repository import FileRepository
from src.service.car_service import CarService
from src.ui.console import CarConsole


def main():
    car_repository = FileRepository('../data/cars')
    car_service = CarService(car_repository)
    # car_console = CarConsole(car_service)
    console = CarConsole(car_service)
    console.run_commands()

main()