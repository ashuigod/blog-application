from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):  # Class names should follow PascalCase
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Corrected the casing
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # Fixed typo: "dafault" -> "default"

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)