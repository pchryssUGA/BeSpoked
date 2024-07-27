# Generated by Django 5.0.7 on 2024-07-27 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("sale_date", models.DateField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "salesperson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.salesperson",
                    ),
                ),
            ],
        ),
    ]
