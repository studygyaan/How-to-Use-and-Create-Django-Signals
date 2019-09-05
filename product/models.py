from django.db import models

# from django.db.models import signals
# from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

# # pre_save method signal
# @receiver(signals.pre_save, sender=Product)
# def check_product_description(sender, instance, **kwargs):

#     if not instance.description:
#         instance.description = 'This is Default Description'
    

# # post_save method
# @receiver(signals.post_save, sender=Product) 
# def create_product(sender, instance, created, **kwargs):
#     print("Save method is called")