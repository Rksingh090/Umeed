# Generated by Django 3.1.2 on 2020-12-11 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile_no', models.IntegerField(max_length=11, null=True)),
                ('massage', models.TextField(null=True)),
            ],
        ),
    ]
