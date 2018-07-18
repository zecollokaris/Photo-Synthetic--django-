from django.test import TestCase
from .models import Image,Location,Category
'''End Of Import'''
#---------------------------------------------------------------------#


# TESTS HERE!


#################################################################################################################################################################################
#IMAGE TESTS HERE
#################################################################################################################################################################################

#IMAGE Tests!

class ImageTestClass(TestCase):
    
    def setUp(self):

        self.category = Category(category_name='Portrait')
        self.category.save()

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

#################################################################################################################################################################################