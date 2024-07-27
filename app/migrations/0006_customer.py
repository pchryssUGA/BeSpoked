# Generated by Django 5.0.7 on 2024-07-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_salesperson_delete_testtable"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("start_date", models.DateField()),
            ],
            options={
                "db_table": "Customer",
                "managed": False,
            },
        ),
    ]
