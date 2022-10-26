# Generated by Django 4.1.2 on 2022-10-26 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0002_remove_attraction_distance_alter_attraction_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(default=5)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.attraction')),
            ],
        ),
    ]
