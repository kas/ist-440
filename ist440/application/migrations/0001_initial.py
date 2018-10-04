# Generated by Django 2.1.2 on 2018-10-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MapMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('x_coordinate', models.DecimalField(decimal_places=3, max_digits=6)),
                ('y_coordinate', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
    ]