from django.db import models
import csv  
class CardTransactions(models.Model):
    series_reference = models.CharField(max_length=255)
    period = models.CharField(max_length=255, null= True, blank=True)
    data_value = models.FloatField(null= True, blank=True)
    status = models.CharField(max_length=255, null= True, blank=True)
    units = models.CharField(max_length=255, null= True, blank=True)
    magnitude = models.IntegerField(null= True, blank=True)
    subject = models.CharField(max_length=255, null= True, blank=True)
    group = models.CharField(max_length=255, null= True, blank=True)
    series_title_1 = models.CharField(max_length=255, null= True, blank=True)
    series_title_2 = models.CharField(max_length=255, null= True, blank=True)

    def __str__(self):
        return self.series_reference
    
    @classmethod
    def insert_rows_from_csv(cls, file):
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)

        for row in reader:
            try:
                obj = cls.objects.create(
                    series_reference=row[0],
                    period=row[1],
                    data_value=float(row[2]),
                    status=row[3],
                    units=row[4],
                    magnitude=int(row[5]),
                    subject=row[6],
                    group=row[7],
                    series_title_1=row[8],
                    series_title_2=row[9],
                )
                obj.save()
            except Exception as e:
                print("error:",e)

        