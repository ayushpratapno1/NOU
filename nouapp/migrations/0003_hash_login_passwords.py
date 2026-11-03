from django.contrib.auth.hashers import identify_hasher, make_password
from django.db import migrations, models


def hash_legacy_passwords(apps, schema_editor):
    login_model = apps.get_model('nouapp', 'Login')
    for login in login_model.objects.all().iterator():
        try:
            identify_hasher(login.password)
        except ValueError:
            login.password = make_password(login.password)
            login.save(update_fields=['password'])


class Migration(migrations.Migration):
    dependencies = [
        ('nouapp', '0002_alter_student_rollno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.RunPython(
            hash_legacy_passwords,
            migrations.RunPython.noop,
        ),
    ]
