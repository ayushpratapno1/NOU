from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from adminapp.models import Branch, Program, Year
from .models import Login, Student
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
        legacy_login = Login.objects.create(
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
        legacy_login.refresh_from_db()
        self.assertTrue(legacy_login.check_password("student-password"))
        self.assertNotEqual(legacy_login.password, "student-password")

    def test_registration_hashes_password_and_allows_login(self):
        response = self.client.post(
            reverse("nouapp:registration"),
            {
                "rollno": "student-2",
                "name": "Student",
                "fname": "Father",
                "mname": "Mother",
                "gender": "male",
                "address": "Address",
                "program": "B.Tech.",
                "branch": "Computer Science",
                "year": "First Year",
                "contactno": "1234567890",
                "emailaddress": "student-2@example.com",
                "password": "student-password",
                "confirmpassword": "student-password",
            },
        )

        self.assertEqual(response.status_code, 200)
        login_record = Login.objects.get(userid="student-2")
        self.assertTrue(login_record.check_password("student-password"))
        self.assertNotEqual(login_record.password, "student-password")

        response = self.client.post(
            reverse("nouapp:login"),
            {
                "userid": "student-2",
                "password": "student-password",
                "usertype": "student",
            },
        )
        self.assertRedirects(response, reverse("studentapp:studenthome"))

    def test_hashed_student_login_rejects_wrong_password(self):
        login_record = Login(userid="student-3", usertype="student", status="false")
        login_record.set_password("student-password")
        login_record.save()

        response = self.client.post(
            reverse("nouapp:login"),
            {
                "userid": "student-3",
                "password": "wrong-password",
                "usertype": "student",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid User")

    def test_hashed_custom_admin_login_still_works(self):
        login_record = Login(userid="portal-admin", usertype="admin", status="true")
        login_record.set_password("admin-password")
        login_record.save()

        response = self.client.post(
            reverse("nouapp:login"),
            {
                "userid": "portal-admin",
                "password": "admin-password",
                "usertype": "admin",
            },
        )

        self.assertRedirects(response, reverse("adminapp:adminhome"))
        self.assertEqual(self.client.session["adminid"], "portal-admin")

    def test_change_password_verifies_and_hashes_password(self):
        Student.objects.create(
            rollno="student-4",
            name="Student",
            fname="Father",
            mname="Mother",
            gender="male",
            address="Address",
            program="B.Tech.",
            branch="Computer Science",
            year="First Year",
            contactno="1234567890",
            emailaddress="student-4@example.com",
            regdate="2026-01-01",
        )
        login_record = Login(userid="student-4", usertype="student", status="false")
        login_record.set_password("old-password")
        login_record.save()
        session = self.client.session
        session["rollno"] = "student-4"
        session.save()

        response = self.client.post(
            reverse("studentapp:changepassword"),
            {
                "oldpassword": "old-password",
                "newpassword": "new-password",
                "confirmpassword": "new-password",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("studentapp:studentlogout"))
        login_record.refresh_from_db()
        self.assertTrue(login_record.check_password("new-password"))
        self.assertFalse(login_record.check_password("old-password"))

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
