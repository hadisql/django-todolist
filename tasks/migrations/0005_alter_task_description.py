# Generated by Django 4.2.1 on 2023-06-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0004_alter_task_description_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
