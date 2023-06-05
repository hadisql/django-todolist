# Generated by Django 4.2.1 on 2023-06-03 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0006_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "1: Low"), (2, "2: Normal"), (3, "3: High")],
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(3),
                ],
            ),
        ),
    ]
