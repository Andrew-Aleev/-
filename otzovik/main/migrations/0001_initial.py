# Generated by Django 4.1.5 on 2023-05-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('number1', models.CharField(blank=True, max_length=50)),
                ('number2', models.CharField(blank=True, max_length=50)),
                ('number3', models.CharField(blank=True, max_length=50)),
                ('number4', models.CharField(blank=True, max_length=50)),
                ('number5', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Opros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=255)),
                ('number1', models.CharField(max_length=2)),
                ('number2', models.CharField(max_length=2)),
                ('number3', models.CharField(max_length=2)),
                ('number4', models.CharField(max_length=2)),
                ('number5', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=50)),
                ('date_of_dirth', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=12)),
                ('image', models.ImageField(upload_to='qr_codes/')),
            ],
        ),
    ]
