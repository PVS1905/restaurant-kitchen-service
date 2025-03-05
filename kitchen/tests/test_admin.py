from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="<PASSWORD>"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_superuser(
            username="Cook",
            password="<PASSWORD>",
            years_of_experience="8"
        )

    def test_cook_years_of_experience(self):
        url = reverse("admin:kitchen_cook_changelist")
        result = self.client.get(url)
        self.assertContains(result, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.pk])
        result = self.client.get(url)
        self.assertContains(result, self.cook.years_of_experience)

    def test_cook_additional_info(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.pk])
        result = self.client.get(url)
        self.assertContains(result, self.cook.first_name)
        self.assertContains(result, self.cook.last_name)
        self.assertContains(result, self.cook.years_of_experience)
