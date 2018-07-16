from django.db import models

# Created models

class Location(models.Model):
    #Attribute Variables of class Location
    name = models.CharField(max_length=20)

    '''Method to filter database results'''
    def __str__(self):
        return self.name


class Category(models.Model):
    #Attribute Variables of class Category
    name = models.CharField(max_length=20)

    '''Method to filter database results'''
    def __str__(self):
        return self.name

    

class Image(models.Model):  
    #Attribute Variables of class Image
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to ='pics/')
    description = models.CharField(max_length=250)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null='True', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null='True', blank=True)

    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__name__icontains=search_term).all()
        return image

    '''Method to filter database results'''
    def __str__(self):
        return self.name

    