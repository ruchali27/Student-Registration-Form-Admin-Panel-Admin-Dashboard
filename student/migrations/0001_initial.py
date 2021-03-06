# Generated by Django 3.2.6 on 2021-11-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mob_no', models.IntegerField()),
                ('profile_img', models.ImageField(upload_to='')),
                ('DOB', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
