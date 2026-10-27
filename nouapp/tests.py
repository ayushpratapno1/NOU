from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Login


class LoginTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.password = "A-valid-password-123!"
        self.superuser = self.user_model.objects.create_superuser(
            username="deployment-admin",
            email="deployment-admin@example.com",
            password=self.password,
        )

    def test_superuser_can_login_through_public_login(self):
        response = self.client.post(
            reverse("nouapp:login"),
            {
                "userid": self.superuser.username,
                "password": self.password,
                "usertype": "admin",
            },
        )

        self.assertRedirects(response, reverse("adminapp:adminhome"))
        self.assertEqual(self.client.session["adminid"], self.superuser.username)
        self.assertEqual(self.client.session["_auth_user_id"], str(self.superuser.pk))

    def test_legacy_student_login_still_works(self):
        Login.objects.create(
            userid="student-1",
            password="student-password",
            usertype="student",
            status="false",
        )

        response = self.client.post(
            reverse("nouapp:login"),
            {
                "userid": "student-1",
                "password": "student-password",
                "usertype": "student",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("studentapp:studenthome"))

    def test_superuser_can_login_through_django_admin(self):
        response = self.client.post(
            reverse("admin:login"),
            {
                "username": self.superuser.username,
                "password": self.password,
                "next": reverse("admin:index"),
            },
        )

        self.assertRedirects(response, reverse("admin:index"))
