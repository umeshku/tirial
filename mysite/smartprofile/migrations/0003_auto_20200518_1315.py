# Generated by Django 3.0.6 on 2020-05-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartprofile', '0002_auto_20200420_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='SubmissionDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='Survyour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]
