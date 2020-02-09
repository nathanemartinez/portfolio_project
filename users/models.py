from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pictures')

    def __str__(self):
        return self.user

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     # This resizes the image if it's bigger than 700x700
    #     # You can also delete the previous image when the user successfully
    #     # changes their profile image
    #     if img.height > 700 or img.width > 700:
    #         output_size = (700, 700)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    #
