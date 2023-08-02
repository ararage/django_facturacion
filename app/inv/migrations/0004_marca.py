# Generated by Django 2.2 on 2023-08-01 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inv", "0003_subcategoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("estado", models.BooleanField(default=True)),
                ("fc", models.DateTimeField(auto_now_add=True)),
                ("fm", models.DateTimeField(auto_now=True)),
                ("um", models.IntegerField(blank=True, null=True)),
                (
                    "descripcion",
                    models.CharField(
                        help_text="Descripción de la Marca", max_length=100, unique=True
                    ),
                ),
                (
                    "uc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Marca",
            },
        ),
    ]
