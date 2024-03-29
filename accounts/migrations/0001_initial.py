# Generated by Django 3.2.8 on 2021-10-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=40)),
                ('employeeId', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science & Engineering (CSE)'), ('IT', 'Information Technology (IT)'), ('SF', 'Fire & Safety (SE)'), ('ME', 'Mechanical Engineering (ME)'), ('ECE', 'Electronics & Communication (ECE)'), ('EEE', 'Electrical & Electronics (EEE')], default='Computer Science & Engineering (CSE)', max_length=4)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
