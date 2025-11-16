from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from .models import Products

@receiver(pre_save, sender = Products)
def preproduct_save(sender, instance, *args, **kwargs):
    print(f"DEBUG (pre_save): {instance.product_name} is being added to the list of products.")

@receiver(post_save, sender = Products)
def postproduct_save(sender, instance, created, *args, **kwargs):
    if created:
        print(f"DEBUG (post_save): Successfully added {instance.product_name} in the list of products.")
    else:
        print(f"DEBUG (post_save): Successfully updated an existing product: {instance.product_name}.")

@receiver(pre_delete, sender = Products)
def preproduct_delete(sender, instance, *args, **kwargs):
    print(f"DEBUG (post_delete): WARNING! The following product is about to get permanently deleted: {instance.product_name}")

@receiver(post_delete, sender = Products)
def postproduct_delete(sender, instance, *args, **kwargs):
    print(f"DEBUG (post_delete): The following product has been deleted successfully: {instance.product_name}") 
   