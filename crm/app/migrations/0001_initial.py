# Generated by Django 5.0.2 on 2024-03-12 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contract",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "document",
                    models.FileField(
                        blank=True, null=True, upload_to="contracts/documents/"
                    ),
                ),
                ("created_at", models.DateTimeField(null=True)),
                ("validity_period", models.IntegerField(default=0)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=None, max_digits=10),
                ),
            ],
        ),
    ]
