# Generated by Django 3.2.4 on 2021-06-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambridgelevel',
            name='level',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='gottengrade',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
