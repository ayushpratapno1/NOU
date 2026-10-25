#!/usr/bin/env python
"""Create the initial Django superuser once during a deployment build."""

import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "egyanproject.settings")
django.setup()

from django.contrib.auth import get_user_model  # noqa: E402


USERNAME_ENV = "SUPERUSER_USERNAME"
EMAIL_ENV = "SUPERUSER_EMAIL"
PASSWORD_ENV = "SUPERUSER_PASSWORD"


def main():
    user_model = get_user_model()

    username = os.getenv(USERNAME_ENV, "").strip()
    email = os.getenv(EMAIL_ENV, "").strip()
    password = os.getenv(PASSWORD_ENV, "")

    missing = [
        variable
        for variable, value in (
            (USERNAME_ENV, username),
            (EMAIL_ENV, email),
            (PASSWORD_ENV, password),
        )
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Cannot create the initial superuser. Set these Render environment "
            f"variables: {', '.join(missing)}"
        )

    if user_model.objects.filter(username=username, is_superuser=True).exists():
        print(f"Superuser '{username}' already exists. Skipping creation.")
        return

    if user_model.objects.filter(username=username).exists():
        raise RuntimeError(
            f"Cannot create superuser: username '{username}' already belongs "
            "to a non-superuser account."
        )

    user_model.objects.create_superuser(
        username=username,
        email=email,
        password=password,
    )
    print(f"Created superuser '{username}'.")


if __name__ == "__main__":
    main()
