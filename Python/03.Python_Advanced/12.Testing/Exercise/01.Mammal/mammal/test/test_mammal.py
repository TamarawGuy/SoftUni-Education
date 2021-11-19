from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Manol", "Manolov", "Bitcoin")

    def test_init_atr(self):
        self.assertEqual("Manol", self.mammal.name)
        self.assertEqual("Manolov", self.mammal.type)
        self.assertEqual("Bitcoin", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Manol makes Bitcoin", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        self.assertEqual("Manol is of type Manolov", self.mammal.info())


if __name__ == "__main__":
    main()
