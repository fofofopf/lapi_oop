if __name__ == "__main__":
    class Vehicle:
        def __init__(self, make: str, model: str, year: int):
            """
            Конструктор базового класса Vehicle.

            Args:
                make (str): Марка транспортного средства.
                model (str): Модель транспортного средства.
                year (int): Год выпуска транспортного средства.
            """
            self._make = make
            self._model = model
            self._year = year

        @property
        def make(self) -> str:
            """Марка транспортного средства."""
            return self._make

        @property
        def model(self) -> str:
            """Модель транспортного средства."""
            return self._model

        @property
        def year(self) -> int:
            """Год выпуска транспортного средства."""
            return self._year

        def start_engine(self) -> str:
            """
            Запуск двигателя.

            Returns:
                str: Сообщение о запуске двигателя.
            """
            return f"{self.make} {self.model} двигатель запущен."

        def stop_engine(self) -> str:
            """
            Остановка двигателя.

            Returns:
                str: Сообщение об остановке двигателя.
            """
            return f"{self.make} {self.model} двигатель остановлен."

        def __str__(self) -> str:
            return f"{self.year} {self.make} {self.model}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


    class Car(Vehicle):
        def __init__(self, make: str, model: str, year: int, num_doors: int):
            """
            Конструктор класса Car.

            Args:
                make (str): Марка автомобиля.
                model (str): Модель автомобиля.
                year (int): Год выпуска автомобиля.
                num_doors (int): Количество дверей.
            """
            super().__init__(make, model, year)
            self._num_doors = num_doors

        @property
        def num_doors(self) -> int:
            """Количество дверей."""
            return self._num_doors

        def __str__(self) -> str:
            return f"{super().__str__()} ({self.num_doors} дверей)"

        def drive(self) -> str:
            """
            Запуск двигателя и начало движения.

            Returns:
                str: Сообщение о начале движения.
            """
            return f"{self.make} {self.model} начал движение."

        # Перегрузка метода __repr__ не требуется, так как он унаследован от базового класса


    class Truck(Vehicle):
        def __init__(self, make: str, model: str, year: int, max_payload: float):
            """
            Конструктор класса Truck.

            Args:
                make (str): Марка грузовика.
                model (str): Модель грузовика.
                year (int): Год выпуска грузовика.
                max_payload (float): Максимальная грузоподъемность (в тоннах).
            """
            super().__init__(make, model, year)
            self._max_payload = max_payload

        @property
        def max_payload(self) -> float:
            """Максимальная грузоподъемность (в тоннах)."""
            return self._max_payload

        def __str__(self) -> str:
            return f"{super().__str__()} (грузоподъемность: {self.max_payload} тонн)"

        def load_cargo(self, weight: float) -> str:
            """
            Загрузка груза в грузовик.

            Args:
                weight (float): Вес груза (в тоннах).

            Returns:
                str: Сообщение о загрузке груза.
            """
            if weight <= 0:
                raise ValueError("Вес груза должен быть положительным числом.")
            if weight > self.max_payload:
                return f"Грузовик перегружен. Максимальная грузоподъемность: {self.max_payload} тонн."
            return f"{self.make} {self.model} загружен грузом весом {weight} тонн."

        # Перегрузка метода __repr__ не требуется, так как он унаследован от базового класса


    pass
