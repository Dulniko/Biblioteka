# Generated by Django 4.1.5 on 2023-02-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_customer_alter_loan_borrower"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]
