from django.db import models


'''End Of Import'''
#---------------------------------------------------------------------#


# MODELS CREATED HERE!

#################################################################################################################################################################################
# MODEL LOCATION!
#################################################################################################################################################################################

#...Class LOCATION added here...
class Location(models.Model):
    #Attribute Variables of class Location
    name = models.CharField(max_length=20)

    '''Method to filter database results'''
    def __str__(self):
        return self.name

#################################################################################################################################################################################
# MODEL CATEGORY WHERE IMAGES ARE GROUPED IN!
#################################################################################################################################################################################

#...Class CATEGORY added here...
class Category(models.Model):
    #Attribute Variables of class Category
    name = models.CharField(max_length=20)

    '''Method to filter database results'''
    def __str__(self):
        return self.name

#################################################################################################################################################################################
# MODEL IMAGE WHICH IS THE IMAGES ADDED!
#################################################################################################################################################################################

#...Class IMAGE added here...
class Image(models.Model):  
    #Attribute Variables of class Image
    '''
    name-: Name of picture taken.
    image-: This is posted Image.
    description-: This is the description of the image posted.
    location-: This is the location the picture was taken at.
    category-: This is the category the image is placed in.
    '''
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

#################################################################################################################################################################################
