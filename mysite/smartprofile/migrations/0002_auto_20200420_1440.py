# Generated by Django 3.0.4 on 2020-04-20 08:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('smartprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='KEY',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
