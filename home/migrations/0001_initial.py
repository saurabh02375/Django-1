# Generated by Django 5.1.4 on 2025-01-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=122)),
                ("description", models.CharField(max_length=122)),
                ("date", models.DateField()),
            ],
        ),
    ]
