# Generated by Django 5.0.6 on 2024-08-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_remove_employee_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
