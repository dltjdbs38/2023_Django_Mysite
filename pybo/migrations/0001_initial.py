# Generated by Django 4.2.2 on 2023-06-14 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("subject", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, # id가 자동으로 1,2,3,4 증가하여 부여
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ), ## id - 데이터에는 무결성이 있어야 한다. 내용이 아예 똑같은 
                    # 데이터가 들어올 수 있으므로 고유한 id 부여.
                ),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField()),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pybo.question"
                    ),
                ),
            ],
        ),
    ]
