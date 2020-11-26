from django.db import models

# Create your models here.
class Asset(models.Model):
    a_lot_no = models.CharField(max_length=100)
    a_deed_no= models.CharField(max_length=100)
    a_sell_order = models.CharField(max_length=100)
    a_law_suit = models.CharField(max_length=100)
    a_type = models.CharField(max_length=100)
    a_rai = models.CharField(max_length=100)
    a_ngan = models.CharField(max_length=100)
    a_wa = models.CharField(max_length=100)
    a_price = models.CharField(max_length=100)
    a_tumbon = models.CharField(max_length=100)
    a_ampur = models.CharField(max_length=100)
    a_province = models.CharField(max_length=100)
    a_ampur_code = models.CharField(max_length=4)
    a_province_code = models.CharField(max_length=5)
    a_law_suit_no = models.CharField(max_length=50)
    a_law_suit_year = models.CharField(max_length=50)
    a_law_court_id = models.CharField(max_length=50)
    is_chanode = models.CharField(max_length=1)
    
    def __str__(self):
        return self.a_law_suit