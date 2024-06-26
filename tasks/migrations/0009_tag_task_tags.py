# Generated by Django 4.2.1 on 2023-06-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0008_alter_task_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="tasks.tag"
            ),
        ),
    ]
