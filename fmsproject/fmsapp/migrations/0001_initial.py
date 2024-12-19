# Generated by Django 5.1.4 on 2024-12-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('studentid', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Prefer not to say')], max_length=1)),
                ('registrationtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'UserRegistrationTable',
            },
        ),
    ]
