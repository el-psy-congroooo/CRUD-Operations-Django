# Generated by Django 3.1.6 on 2021-02-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pi',
            name='std',
            field=models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th'), ('11', '11th'), ('12', '12th')], max_length=100),
        ),
    ]
