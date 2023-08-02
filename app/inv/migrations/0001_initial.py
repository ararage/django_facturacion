# Generated by Django 2.2 on 2023-07-21 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("fc", models.DateTimeField(auto_now=True)),
                ("um", models.IntegerField(blank=True, null=True)),
                (
                    "descripcion",
                    models.CharField(
                        help_text="Descripción de la categoría",
                        max_length=100,
                        unique=True,
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
                "verbose_name_plural": "Categorias",
            },
        ),
    ]
