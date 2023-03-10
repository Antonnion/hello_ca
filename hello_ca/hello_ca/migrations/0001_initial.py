# Generated by Django 4.1.5 on 2023-02-04 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Depertment",
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
                ("name", models.CharField(max_length=64)),
                (
                    "short_name",
                    models.CharField(
                        choices=[
                            ("BP", "Business Promotion"),
                            ("Tech", "Technique"),
                            ("FO", "Foreign Operation"),
                            ("BA", "Business Administration"),
                        ],
                        max_length=8,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=64)),
                ("intro_text", models.CharField(max_length=256)),
                (
                    "depertment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hello_ca.depertment",
                    ),
                ),
            ],
        ),
    ]
