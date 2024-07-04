# Generated by Django 5.0.6 on 2024-07-04 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
        ('career', '0001_initial'),
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.professor', verbose_name='Director'),
        ),
        migrations.AlterField(
            model_name='career',
            name='level',
            field=models.CharField(choices=[('TSU', 'Técnico Superior Universitario'), ('ING', 'Ingenieria'), ('MTR', 'Maestria'), ('Lic', 'Licenciatura')], max_length=5, verbose_name='Nivel de estudios'),
        ),
        migrations.AlterField(
            model_name='career',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='career',
            name='short_name',
            field=models.CharField(max_length=10, verbose_name='Abreviatura'),
        ),
        migrations.AlterField(
            model_name='career',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='career',
            name='year_plan',
            field=models.CharField(max_length=4, verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='file',
            field=models.CharField(max_length=100, verbose_name='Hoja de asignatura'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Materia'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='period.semester', verbose_name='Semestre'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='total_hours',
            field=models.IntegerField(verbose_name='Horas totales'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='weekly_hours',
            field=models.IntegerField(verbose_name='Horas semanales'),
        ),
    ]
