from django.db import models

# Create your models here.
class champion(models.Model):
    champion_id = models.IntegerField(blank=False, default=0)
    champion_name = models.CharField(max_length=200,blank=False, default='')

    class Meta:
        db_table = "champion"