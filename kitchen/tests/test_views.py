from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen.models import DishType, Dish


class PublicDishTypeTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="Test_dish_type"
        )
        self.LOGIN_URL = reverse("kitchen:index")
        self.DISH_TYPE_LOGIN_URL = reverse("kitchen:dish-type-list")
        self.DISH_TYPE_CREATE_URL = reverse("kitchen:dish-type-create")
        self.DISH_TYPE_UPDATE_URL = reverse(
            "kitchen:dish-type-update",
            args=[self.dish_type.pk]
        )
        self.DISH_TYPE_DELETE_URL = reverse(
            "kitchen:dish-type-delete",
            args=[self.dish_type.pk]
        )

    def test_login_index(self):
        result = self.client.get(self.LOGIN_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_login_dish_type(self):
        result = self.client.get(self.DISH_TYPE_LOGIN_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_create_dish_type(self):
        result = self.client.get(self.DISH_TYPE_CREATE_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_update_dish_type(self):
        result = self.client.get(self.DISH_TYPE_UPDATE_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_delete_dish_type(self):
        result = self.client.get(self.DISH_TYPE_DELETE_URL)
        self.assertNotEqual(result.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Cook",
            password="test123",
        )
        self.client.force_login(self.user)
        DishType.objects.create(
            name="Dish type 1"
        )
        DishType.objects.create(
            name="Dish type 2"
        )

    def test_retrieve_dish_type(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")


class PublicDishTest(TestCase):
    def setUp(self):
        dish_type = DishType.objects.create(
            name="Dish type"
        )
        self.dish = Dish.objects.create(
            name="Dish",
            dish_type=dish_type,
            description="A classic dish with a modern twist.",
            price=10.20,
        )
        self.DISH_LIST_URL = reverse("kitchen:dish-list")
        self.DISH_LOGIN_DETAIL_URL = reverse(
            "kitchen:dish-detail",
            args=[self.dish.pk]
        )
        self.DISH_CREATE_URL = reverse("kitchen:dish-create")
        self.DISH_UPDATE_URL = reverse(
            "kitchen:dish-update",
            args=[self.dish.pk]
        )
        self.DISH_DELETE_URL = reverse(
            "kitchen:dish-delete",
            args=[self.dish.pk]
        )

    def test_login_dish(self):
        result = self.client.get(self.DISH_LIST_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_login_detail_dish(self):
        result = self.client.get(self.DISH_LOGIN_DETAIL_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_create_dish(self):
        result = self.client.get(self.DISH_CREATE_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_update_dish(self):
        result = self.client.get(self.DISH_UPDATE_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_delete_dish(self):
        result = self.client.get(self.DISH_DELETE_URL)
        self.assertNotEqual(result.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Cook",
            password="test123",
        )
        self.dish_type = DishType.objects.create(
            name="Dish type"
        )
        self.client.force_login(self.user)
        self.dish1 = Dish.objects.create(
            name="Dish_1",
            dish_type=self.dish_type,
            description="A classic dish with a modern twist.",
            price=10
        )
        self.dish2 = Dish.objects.create(
            name="Dish_2",
            dish_type=self.dish_type,
            description="A classic dish with a modern twist.",
            price=12
        )

    def test_retrieve_dishes(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")


class PublicCookTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="Cook",
            first_name="First",
            last_name="Last",
            years_of_experience=10
        )
        self.COOK_LIST_URL = reverse(
            "kitchen:cook-list"
        )
        self.COOK_LOGIN_DETAIL_URL = reverse(
            "kitchen:cook-detail",
            args=[self.cook.pk]
        )
        self.COOK_CREATE_URL = reverse(
            "kitchen:cook-create"
        )
        self.COOK_UPDATE_URL = reverse(
            "kitchen:cook-update",
            args=[self.cook.pk]
        )
        self.COOK_DELETE_URL = reverse(
            "kitchen:cook-delete",
            args=[self.cook.pk]
        )

    def test_login_cook(self):
        result = self.client.get(self.COOK_LIST_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_login_detail_cook(self):
        result = self.client.get(self.COOK_LOGIN_DETAIL_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_create_cook(self):
        result = self.client.get(self.COOK_CREATE_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_update_cook(self):
        result = self.client.get(self.COOK_UPDATE_URL)
        self.assertNotEqual(result.status_code, 200)

    def test_delete_cook(self):
        result = self.client.get(self.COOK_DELETE_URL)
        self.assertNotEqual(result.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Cook",
            password="test123",
            years_of_experience=1
        )
        self.client.force_login(self.user)
        self.cook1 = get_user_model().objects.create_user(
            username="Cook 2",
            password="test123",
            years_of_experience=2
        )
        self.cook2 = get_user_model().objects.create_user(
            username="Cook 3",
            password="test123",
            years_of_experience=2
        )

    def test_retrieve_cooks(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cook1.username)
        self.assertContains(response, self.cook2.username)
        cooks = get_user_model().objects.all()
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")
