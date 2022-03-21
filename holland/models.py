from django.db import models

# Create your models here.
class Crop(models.Model):

    category=(('Crop','Crop'),
                ('Vegetable','Vegetable'),
                ('Plantation','Plantation'),
                ('Commercial crop','Commercial crop')
                )
    category=models.CharField(max_length=20,choices=category)
    name=models.CharField(max_length=20)
    about=models.TextField(max_length=None)
    image=models.ImageField(null=True,blank=True,upload_to="crop-image")

    def __Str__(self):
        return f"{self.name}"


class dealer(models.Model):
    name=models.TextField(max_length=20)
    dealer_code=models.IntegerField(unique=True,primary_key=True)
    dealer_password=models.SlugField(max_length=10,default='123abc')
    address=models.TextField(max_length=20)
    photo=models.ImageField(null=True,blank=True)

    def __str__(self):
        return f"{self.name} {self.dealer_code}"

class farmer_detail(models.Model):
    farmer_dealer_code=models.ForeignKey(dealer,on_delete=models.SET_DEFAULT,default=111999)
    name=models.TextField(max_length=40)
    farmer_panjiyan=models.IntegerField()
    farmer_block=models.TextField(max_length=40)
    farmer_district=models.TextField(max_length=20)
    farmer_village=models.TextField(max_length=20)
    farmer_panchayat=models.TextField(max_length=20)

    def __str__(self):
        return f"{self.farmer_dealer_code} {self.name}"


class survey(models.Model):
    code=models.TextField(max_length=20)
    name=models.TextField(max_length=20)
    namep=models.TextField(max_length=20)
    regd=models.IntegerField()
    number=models.IntegerField()
    system=models.TextField(max_length=20)
    spacing=models.TextField(max_length=20)
    crop=models.TextField(max_length=20)
    pump=models.TextField(max_length=20)
    area=models.TextField(max_length=20)
    type=models.TextField(max_length=20)

    def __str__(self):
        return f'{self.code} {self.name}'


        
