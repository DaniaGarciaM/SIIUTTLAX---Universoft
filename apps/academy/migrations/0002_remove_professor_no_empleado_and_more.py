# Generated by Django 5.0.6 on 2024-07-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='no_empleado',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='puesto_id',
        ),
        migrations.AddField(
            model_name='professor',
            name='employee_number',
            field=models.CharField(default='0000', max_length=5, verbose_name='No. Empleado'),
        ),
    ]
