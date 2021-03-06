# Generated by Django 3.1.7 on 2021-06-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookstb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=30)),
                ('Bookstock', models.PositiveIntegerField()),
                ('Author', models.CharField(default='', max_length=30)),
                ('Publications', models.CharField(default='', max_length=30)),
                ('Price', models.PositiveIntegerField()),
                ('Edition', models.CharField(default='', max_length=30)),
                ('Dateofpublications', models.DateField()),
                ('Photo', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
