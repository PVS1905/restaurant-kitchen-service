from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen.models import DishType, Dish


class ModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Dish_Type",
        )
        expected_str = f"{dish_type.name}"
        self.assertEqual(str(dish_type), expected_str)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="Cook",
            first_name="First",
            last_name="Last",
            password="<PASSWORD>"
        )
        expected_str = (f"{cook.username} "
                        f"({cook.first_name} {cook.last_name})")
        self.assertEqual(str(cook), expected_str)
        self.assertEqual(cook.password, "<PASSWORD>")

    def test_cook_years_of_experience(self):
        cook = get_user_model().objects.create_user(
            username="Cook",
            first_name="First",
            last_name="Last",
            years_of_experience=10
        )
        self.assertEqual(int(cook.years_of_experience), 10)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Dish_Type",
        )
        dish = Dish.objects.create(
            name="Dish",
            description="A classic dish with a modern twist.",
            price=10.20,
            dish_type=dish_type
        )
        self.assertEqual(str(dish.name), dish.name)
