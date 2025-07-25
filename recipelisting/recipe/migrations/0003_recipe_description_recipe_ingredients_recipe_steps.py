# Generated by Django 5.2.4 on 2025-07-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rename_title_recipe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='Unknown ingredients'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.TextField(default='No steps provided'),
        ),
    ]
