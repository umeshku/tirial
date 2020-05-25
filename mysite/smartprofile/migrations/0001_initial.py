# Generated by Django 3.0.4 on 2020-04-09 07:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('SubmissionDate', models.DateTimeField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('Survyour', models.CharField(max_length=100)),
                ('Ward', models.IntegerField()),
                ('Tol', models.CharField(max_length=100)),
                ('HouseCode', models.CharField(max_length=10)),
                ('RoadName', models.CharField(max_length=100)),
                ('HousePhoto', models.CharField(max_length=50)),
                ('GPS_Latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('GPS_Longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('GPS_Altitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('GPS_Accuracy', models.DecimalField(decimal_places=6, max_digits=9)),
                ('Funcational_Type', models.IntegerField(choices=[(1, '1. आवासीय (Residential )'), (2, '2. हुलाक घर (Post Office)'), (3, '3. होस्पितल (Hospital)'), (4, '4. हेल्थ पोस्ट (Health Post)'), (5, '5. क्लिनिक (Clinic)'), (6, '6. वार्ड ओफिस (Ward Office)'), (7, '7. नगरपालिकाको कार्यालय (Municipality Office)'), (8, '8. NTC/Ncell (NTC/Ncell)'), (9, '9. बैंक (Bank)'), (10, '10. शोपिंग महल (Shopping Mall)'), (11, '11. आर्मी कम्प (Army Camp)'), (12, '12. ससत्र प्रहरी बल (Armed Police Force)'), (13, '13. प्रहरी चौकी (police Station)'), (14, '14. मन्दिर (Temple)'), (15, '15. गुम्बाघर (Monestery)'), (16, '16. चर्च (Church)'), (17, '17. मस्जित (Masjit)'), (18, '18. गुठि (Guthi)'), (19, '19. पार्क (Park)'), (20, '20. पर्तिक्छालय (Partikyshalaya)'), (21, '21. पुस्तकालय (Library)'), (22, '22. पसल (Shop)'), (23, '23. सरकारी भवन (GOV Sub Categary)'), (24, '24. सहकारी (Cooperative)'), (25, '25. बिधालय (School)'), (26, '26. कलेज/ कम्पस (Campus/College)'), (27, '27. सभा गृह (City Hall)'), (28, '28. सिनेमा हल (Cinema Hall)'), (29, '29. नर्सिंग होम (Nursing Home)'), (30, '30. बहु उधेस्य  (Multi Purposed)'), (31, '31. गैर सरकारी/अन्तरास्ट्रिय संथा (NGO/INGO)')], default=1)),
                ('KEY', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Ward', models.IntegerField()),
                ('PARENT_KEY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartprofile.Household')),
            ],
        ),
    ]