# Generated by Django 3.2.4 on 2021-06-23 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.cities'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.countries'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
