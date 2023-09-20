# Generated by Django 4.2.5 on 2023-09-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Object_Data",
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
                ("Object_Id", models.IntegerField()),
                ("Name", models.CharField(max_length=50)),
                ("Object_Dimensions", models.CharField(max_length=50)),
            ],
        ),
    ]
