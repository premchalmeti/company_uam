# Generated by Django 3.2.6 on 2021-08-05 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companyrole'),
        ),
    ]
