# Generated by Django 2.2 on 2023-07-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inv", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoria",
            name="fm",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="categoria",
            name="fc",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
