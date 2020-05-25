from django.db import models
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.
class Household(models.Model):
    SubmissionDate=models.DateTimeField(null=True)
    start=models.DateTimeField(null=True)
    end=models.DateTimeField(null=True)
    Survyour=models.CharField(null=True, max_length=100)
    Ward=models.IntegerField(null=True)
    Tol=models.CharField(max_length=100)
    HouseCode=models.CharField(max_length=10)
    RoadName=models.CharField(max_length=100)
    HousePhoto=models.CharField(max_length=50)
    GPS_Latitude=models.DecimalField(null=True, max_digits=19, decimal_places=6)
    GPS_Longitude=models.DecimalField(null=True, max_digits=19, decimal_places=6)
    GPS_Altitude=models.DecimalField(null=True, max_digits=19, decimal_places=6)
    GPS_Accuracy=models.DecimalField(null=True, max_digits=19, decimal_places=6)
    FuncationalChoice=[
    (1 , '1. आवासीय (Residential )') ,
    (2 , '2. हुलाक घर (Post Office)') ,
    (3 , '3. होस्पितल (Hospital)') ,
    (4 , '4. हेल्थ पोस्ट (Health Post)') ,
    (5 , '5. क्लिनिक (Clinic)') ,
    (6 , '6. वार्ड ओफिस (Ward Office)') ,
    (7 , '7. नगरपालिकाको कार्यालय (Municipality Office)') ,
    (8 , '8. NTC/Ncell (NTC/Ncell)') ,
    (9 , '9. बैंक (Bank)') ,
    (10 , '10. शोपिंग महल (Shopping Mall)') ,
    (11 , '11. आर्मी कम्प (Army Camp)') ,
    (12 , '12. ससत्र प्रहरी बल (Armed Police Force)') ,
    (13 , '13. प्रहरी चौकी (police Station)') ,
    (14 , '14. मन्दिर (Temple)') ,
    (15 , '15. गुम्बाघर (Monestery)') ,
    (16 , '16. चर्च (Church)') ,
    (17 , '17. मस्जित (Masjit)') ,
    (18 , '18. गुठि (Guthi)') ,
    (19 , '19. पार्क (Park)') ,
    (20 , '20. पर्तिक्छालय (Partikyshalaya)') ,
    (21 , '21. पुस्तकालय (Library)') ,
    (22 , '22. पसल (Shop)') ,
    (23 , '23. सरकारी भवन (GOV Sub Categary)') ,
    (24 , '24. सहकारी (Cooperative)') ,
    (25 , '25. बिधालय (School)') ,
    (26 , '26. कलेज/ कम्पस (Campus/College)') ,
    (27 , '27. सभा गृह (City Hall)') ,
    (28 , '28. सिनेमा हल (Cinema Hall)') ,
    (29 , '29. नर्सिंग होम (Nursing Home)') ,
    (30 , '30. बहु उधेस्य  (Multi Purposed)') ,
    (31 , '31. गैर सरकारी/अन्तरास्ट्रिय संथा (NGO/INGO)') ,
    ]
    Funcational_Type=MultiSelectField(null=False, choices=FuncationalChoice, default=1)


    KEY=models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            f=getattr(self, field.name, '')
            field_values.append(str(f))
        return ','.join(field_values)


class Personal(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    Ward=models.IntegerField()
    PARENT_KEY=models.ForeignKey(Household, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Ward}, {self.Name}, {self.Age}, {self.PARENT_KEY}"
