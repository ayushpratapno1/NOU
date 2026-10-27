from django.db import migrations, models


def deduplicate_academic_options(apps, schema_editor):
    database = schema_editor.connection.alias

    for model_name, field_name in (
        ("Program", "program"),
        ("Branch", "branch"),
        ("Year", "year"),
    ):
        model = apps.get_model("adminapp", model_name)
        seen = set()

        for option in model.objects.using(database).order_by("pk"):
            value = " ".join(getattr(option, field_name).split())
            key = value.casefold()

            if key in seen:
                option.delete(using=database)
                continue

            if value != getattr(option, field_name):
                setattr(option, field_name, value)
                option.save(using=database, update_fields=[field_name])

            seen.add(key)


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0004_seed_academic_options"),
    ]

    operations = [
        migrations.RunPython(
            deduplicate_academic_options,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="program",
            name="program",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="branch",
            name="branch",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="year",
            name="year",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
