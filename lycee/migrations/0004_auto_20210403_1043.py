# Generated by Django 3.1.7 on 2021-04-03 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0003_presence'),
    ]

    operations = [
        migrations.AddField(
            model_name='presence',
            name='time_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='presence',
            name='time_start',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Appel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('cursus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.cursus')),
            ],
        ),
        migrations.AddField(
            model_name='presence',
            name='appel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.appel'),
        ),
    ]
