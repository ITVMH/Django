# Generated by Django 3.2.4 on 2021-06-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=23)),
                ('ename', models.CharField(max_length=123)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]