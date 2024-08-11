 


from django.db import models
from django.contrib.auth.models import User

# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     row_data = models.TextField()

class Favorite(models.Model):
    # on_delete=models.CASCADE means that when the referenced User is deleted, all related Favorite instances will also be deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    row_data = models.TextField()  # or use a more appropriate field type

    class Meta:
        unique_together = ('user', 'row_data')