# Generated by Django 3.1.1 on 2020-09-17 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffePod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_type', models.CharField(choices=[('COFFEE_POD_LARGE', 'COFFEE_POD_LARGE'), ('COFFEE_POD_SMALL', 'COFFEE_POD_SMALL'), ('ESPRESSO_POD', 'ESPRESSO_POD')], max_length=60)),
                ('flavor_type', models.CharField(choices=[('COFFEE_FLAVOR_VANILLA', 'COFFEE_FLAVOR_VANILLA'), ('COFFEE_FLAVOR_CARAMEL', 'COFFEE_FLAVOR_CARAMEL'), ('COFFEE_FLAVOR_PSL', 'COFFEE_FLAVOR_PSL'), ('COFFEE_FLAVOR_MOCHA', 'COFFEE_FLAVOR_MOCHA'), ('COFFEE_FLAVOR_HAZELNUT', 'COFFEE_FLAVOR_HAZELNUT')], max_length=60)),
                ('size_type', models.CharField(choices=[('1', '1'), ('3', '3'), ('5', '5'), ('7', '7')], max_length=60)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
    ]
