from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero1 = Hero("Tamaraw", 5, 100, 10)

    def test_init_attr(self):
        self.assertEqual("Tamaraw", self.hero1.username)
        self.assertEqual(5, self.hero1.level)
        self.assertEqual(100, self.hero1.health)
        self.assertEqual(10, self.hero1.damage)

    def test_battle_with_hero_with_same_name_raises_exception(self):
        hero2 = Hero("Tamaraw", 5, 100, 10)
        with self.assertRaises(Exception) as ex:
            self.hero1.battle(hero2)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_below_zero_raises_value_error(self):
        self.hero1.health = -50
        hero2 = Hero("Manol", 5, 100, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero1.battle(hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_health_equal_to_zero_raises_value_error(self):
        self.hero1.health = 0
        hero2 = Hero("Manol", 5, 100, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero1.battle(hero2)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_below_zero_raises_value_error(self):
        hero2 = Hero("Manol", 10, -50, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero1.battle(hero2)
        self.assertEqual("You cannot fight Manol. He needs to rest", str(ex.exception))

    def test_battle_enemy_health_equal_to_zero_raises_value_error(self):
        hero2 = Hero("Manol", 10, 0, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero1.battle(hero2)
        self.assertEqual("You cannot fight Manol. He needs to rest", str(ex.exception))

    def test_battle_success_both_healths_above_zero(self):
        hero2 = Hero("Manol", 5, 100, 5)
        self.hero1.battle(hero2)
        self.assertEqual(75, self.hero1.health)
        self.assertEqual(55, hero2.health)

    def test_battle_both_healths_are_zero_draw(self):
        self.hero1.level = 10
        hero2 = Hero("Manol", 10, 100, 10)
        self.assertEqual("Draw", self.hero1.battle(hero2))

    def test_battle_both_healths_are_below_zero_draw(self):
        self.hero1.level = 15
        hero2 = Hero("Manol", 15, 100, 10)
        self.assertEqual("Draw", self.hero1.battle(hero2))

    def test_battle_only_enemy_health_is_below_zero(self):
        hero2 = Hero("Manol", 5, 40, 10)
        result = self.hero1.battle(hero2)
        self.assertEqual(6, self.hero1.level)
        self.assertEqual(55, self.hero1.health)
        self.assertEqual(15, self.hero1.damage)
        self.assertEqual("You win", result)

    def test_battle_only_your_health_is_below_zero(self):
        self.hero1.health = 40
        hero2 = Hero("Manol", 5, 100, 10)
        result = self.hero1.battle(hero2)
        self.assertEqual(6, hero2.level)
        self.assertEqual(55, hero2.health)
        self.assertEqual(15, hero2.damage)
        self.assertEqual("You lose", result)

    def test_battle_only_enemy_health_is_zero(self):
        hero2 = Hero("Manol", 5, 50, 10)
        result = self.hero1.battle(hero2)
        self.assertEqual(6, self.hero1.level)
        self.assertEqual(55, self.hero1.health)
        self.assertEqual(15, self.hero1.damage)
        self.assertEqual("You win", result)

    def test_battle_only_your_health_is_zero(self):
        self.hero1.health = 50
        hero2 = Hero("Manol", 5, 200, 10)
        result = self.hero1.battle(hero2)
        self.assertEqual(6, hero2.level)
        self.assertEqual(155, hero2.health)
        self.assertEqual(15, hero2.damage)
        self.assertEqual("You lose", result)

    def test_str_hero(self):
        result = str(self.hero1)
        self.assertEqual("Hero Tamaraw: 5 lvl\nHealth: 100\nDamage: 10\n", result)


if __name__ == "__main__":
    main()