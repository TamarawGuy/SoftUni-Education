import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 100)

    def test_init_atr(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_capacity_unchanged_when_if_fuel_changed(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_drive_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_refuel_success(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(5)
        self.assertEqual(48.75, self.vehicle.fuel)

    def test_refuel_raises_exception_when_fuel_above_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))


    def test_str_method(self):
        result = str(self.vehicle)
        self.assertEqual("The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    unittest.main()
