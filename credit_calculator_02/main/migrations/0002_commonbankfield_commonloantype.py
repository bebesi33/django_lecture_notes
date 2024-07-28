# Generated by Django 4.2.10 on 2024-07-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommonBankField",
            fields=[
                (
                    "bank",
                    models.CharField(
                        max_length=25,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Commerical Bank",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="CommonLoanType",
            fields=[
                (
                    "loan_type",
                    models.CharField(max_length=25, primary_key=True, serialize=False),
                ),
            ],
            options={"abstract": False,},
        ),
    ]