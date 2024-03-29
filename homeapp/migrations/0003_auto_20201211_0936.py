# Generated by Django 3.1.2 on 2020-12-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_auto_20201211_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('mobile_no', models.IntegerField(null=True)),
                ('property_type', models.CharField(max_length=100, null=True)),
                ('budget', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='modalform',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]
