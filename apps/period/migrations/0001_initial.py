

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('enero - abril', 'enero - abril'), ('mayo - agosto', 'mayo - agosto'), ('septiembre - diciembre', 'septiembre - diciembre')], max_length=25)),
                ('year', models.CharField(max_length=4)),
                ('cicle', models.CharField(default='2023-2024', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('semester_name', models.CharField(max_length=20)),
            ],
        ),
    ]
