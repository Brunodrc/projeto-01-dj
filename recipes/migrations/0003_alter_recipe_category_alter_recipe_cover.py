# Generated by Django 5.1.1 on 2024-10-31 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_is_publiced_recipe_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/'),
        ),
    ]