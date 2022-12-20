# Generated by Django 4.1.3 on 2022-12-16 07:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_dirivinglicence_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dirivinglicence",
            name="comments",
            field=models.TextField(
                max_length=200,
                validators=[
                    django.core.validators.MinLengthValidator(
                        20, "the field must contain at least 20 characters"
                    )
                ],
            ),
        ),
    ]
