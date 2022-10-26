# Generated by Django 4.1.2 on 2022-10-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0004_alter_favorite_attraction_alter_favorite_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.attraction'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
