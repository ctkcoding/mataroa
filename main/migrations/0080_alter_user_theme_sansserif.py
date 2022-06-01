# Generated by Django 4.0.4 on 2022-06-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0079_user_theme_sansserif_alter_user_theme_zialucia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="theme_sansserif",
            field=models.BooleanField(
                default=False,
                help_text="Use sans-serif font in blog content.",
                verbose_name="Theme Sans-serif",
            ),
        ),
    ]
