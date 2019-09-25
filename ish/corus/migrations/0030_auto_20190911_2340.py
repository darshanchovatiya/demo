# Generated by Django 2.2.4 on 2019-09-11 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corus', '0029_auto_20190911_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='rstatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='complain',
            name='cdate',
            field=models.DateField(default=datetime.datetime(2019, 9, 11, 23, 40, 22, 560481)),
        ),
        migrations.AlterField(
            model_name='item',
            name='idate',
            field=models.DateField(default=datetime.datetime(2019, 9, 11, 23, 40, 22, 560481)),
        ),
        migrations.AlterField(
            model_name='order',
            name='odate',
            field=models.DateField(default=datetime.datetime(2019, 9, 11, 23, 40, 22, 560481)),
        ),
        migrations.AlterField(
            model_name='transection',
            name='tdate',
            field=models.DateField(default=datetime.datetime(2019, 9, 11, 23, 40, 22, 560481)),
        ),
    ]
