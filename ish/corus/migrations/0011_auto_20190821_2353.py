# Generated by Django 2.2.4 on 2019-08-21 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corus', '0010_complain_e_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='u_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='corus.Uregiser'),
        ),
    ]
