import unittest
from car_manager import Car


class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("a", 'b', 1, 4)

    def test_init(self):
        self.assertEqual(self.car.make, "a")
        self.assertEqual(self.car.model, "b")
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 4)

    def test_make_raises_exception_when_empty(self):
        with self.assertRaises(Exception):
            self.car.make = ""

    def test_model_raises_exception_when_empty(self):
        with self.assertRaises(Exception):
            self.car.model = ""

    def test_fuel_consumption_when_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -50

    def test_fuel_consumption_when_zero_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

    def test_fuel_capacity_when_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -50

    def test_fuel_capacity_when_zero_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_refuel_more_than_capacity(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_raises_exception_when_negative(self):
        with self.assertRaises(Exception):
            self.car.refuel(-50)

    def test_drive_more_than_fuel(self):
        with self.assertRaises(Exception):
            self.car.drive(1000)

    def test_drive(self):
        self.car.refuel(4)
        self.car.drive(400)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == "__main__":
    unittest.main()