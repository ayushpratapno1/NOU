from django.db import migrations


PROGRAMS = (
    "B.Tech.",
    "M.Tech.",
    "Diploma",
)

BRANCHES = (
    "Computer Science",
    "Information Technology",
    "Electronics Engineering",
)

YEARS = (
    "First Year",
    "Second Year",
    "Third Year",
    "Final Year",
)


def seed_academic_options(apps, schema_editor):
    Program = apps.get_model("adminapp", "Program")
    Branch = apps.get_model("adminapp", "Branch")
    Year = apps.get_model("adminapp", "Year")

    for value in PROGRAMS:
        Program.objects.using(schema_editor.connection.alias).get_or_create(
            program=value
        )
    for value in BRANCHES:
        Branch.objects.using(schema_editor.connection.alias).get_or_create(
            branch=value
        )
    for value in YEARS:
        Year.objects.using(schema_editor.connection.alias).get_or_create(
            year=value
        )


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0003_news"),
    ]

    operations = [
        migrations.RunPython(seed_academic_options, migrations.RunPython.noop),
    ]
