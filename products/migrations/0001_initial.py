# Generated by Django 4.1.7 on 2023-03-10 21:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("stock", models.PositiveIntegerField()),
                ("category", models.CharField(max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
