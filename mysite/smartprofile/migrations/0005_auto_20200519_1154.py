# Generated by Django 3.0.6 on 2020-05-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartprofile', '0004_auto_20200518_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='Ward',
            field=models.IntegerField(null=True),
        ),
    ]