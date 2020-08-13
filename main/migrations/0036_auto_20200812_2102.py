# Generated by Django 3.0.8 on 2020-08-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0035_auto_20200812_2020"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="name",
            field=models.CharField(default="Anonymous", max_length=150, null=True),
        ),
    ]