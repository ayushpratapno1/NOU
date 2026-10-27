from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from adminapp.models import Branch, Program, Year
from .models import Login
from django.db import IntegrityError, transaction

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


class RegistrationOptionsTests(TestCase):
    def test_registration_page_has_academic_options(self):
        response = self.client.get(reverse("nouapp:registration"))

        content = response.content.decode()
        self.assertEqual(content.count('<option value="B.Tech.">'), 1)
        self.assertEqual(content.count('<option value="M.Tech.">'), 1)
        self.assertEqual(content.count('<option value="Diploma">'), 1)
        self.assertEqual(content.count('<option value="Computer Science">'), 1)
        self.assertEqual(
            content.count('<option value="Information Technology">'),
            1,
        )
        self.assertEqual(
            content.count('<option value="Electronics Engineering">'),
            1,
        )
        self.assertEqual(content.count('<option value="First Year">'), 1)
        self.assertEqual(content.count('<option value="Second Year">'), 1)
        self.assertEqual(content.count('<option value="Third Year">'), 1)
        self.assertEqual(content.count('<option value="Final Year">'), 1)
        self.assertTrue(Program.objects.filter(program="B.Tech.").exists())
        self.assertTrue(Branch.objects.filter(branch="Computer Science").exists())
        self.assertTrue(Year.objects.filter(year="First Year").exists())

    def test_academic_options_are_unique_in_database(self):
      self.assertEqual(Program.objects.filter(program="B.Tech.").count(),1,)
      self.assertEqual(Branch.objects.filter(branch="Computer Science").count(),1,)
      self.assertEqual(Year.objects.filter(year="First Year").count(),1,)


    def test_duplicate_program_is_rejected(self):
      with self.assertRaises(IntegrityError):
        with transaction.atomic():
            Program.objects.create(program="B.Tech.")