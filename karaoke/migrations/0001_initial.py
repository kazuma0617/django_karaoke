# Generated by Django 4.1.7 on 2023-06-24 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SongModel",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PointModel",
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
                ("point", models.IntegerField()),
                ("duedate", models.DateField()),
                (
                    "songmodel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="karaoke.songmodel",
                    ),
                ),
            ],
        ),
    ]