from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen.forms import CookCreationForm, CookYearsExperienceUpdateForm


class FormTest(TestCase):
    def test_cook_creation_form(self):
        form_data = {
            "username": "TestCook",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": 5
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        form.save()
        self.assertEqual(form.cleaned_data, form_data)
        response = self.client.post(
            reverse("kitchen:cook-create"),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)
        new_cook = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(
            new_cook.username,
            form_data["username"]
        )
        self.assertEqual(
            new_cook.years_of_experience,
            form_data["years_of_experience"]
        )
        self.assertEqual(
            new_cook.first_name,
            form_data["first_name"]
        )
        self.assertTrue(
            new_cook.check_password(form_data["password1"])
        )

    def test_cook_validate_years_of_experience(self):
        form_data1 = {
            "username": "TestCook1",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": "10 year"
        }
        form1 = CookCreationForm(data=form_data1)
        self.assertFalse(form1.is_valid())
        self.assertIn("years_of_experience", form1.errors)

        form_data2 = {
            "username": "TestCook2",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": "year"
        }
        form2 = CookCreationForm(data=form_data2)
        self.assertFalse(form2.is_valid())
        self.assertIn("years_of_experience", form2.errors)

        form_data3 = {
            "username": "TestCook3",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": 61
        }
        form3 = CookCreationForm(data=form_data3)
        self.assertFalse(form3.is_valid())
        self.assertIn("years_of_experience", form3.errors)

    def test_years_of_experience_update(self):
        cook = get_user_model().objects.create_user(
            username="TestDriver",
            password="password123",
            years_of_experience=1
        )
        form_data = {
            "years_of_experience": 2,
        }

        form = CookYearsExperienceUpdateForm(data=form_data, instance=cook)
        self.assertTrue(form.is_valid(), form.errors)
        updated_cook = form.save()
        # Перевіряємо, що номер посвідчення оновився
        self.assertEqual(updated_cook.years_of_experience, 2)
