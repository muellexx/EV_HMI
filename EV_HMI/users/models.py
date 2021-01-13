from django.db import models
from django.contrib.auth.models import User, Group
from PIL import Image


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = crop_center(img, min(img.size), min(img.size))

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Company(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    image = models.ImageField(default='company_pics/default.jpg', upload_to='company_pics')

    def __str__(self):
        return self.group.name

    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = crop_center(img, min(img.size), min(img.size))

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class CompanyAddress(models.Model):
    COUNTRIES = (
        ('CH', 'Switzerland'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('IT', 'Italy'),
    )
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    address1 = models.CharField("Address Line 1", max_length=100)
    address2 = models.CharField("Address Line 2", max_length=100, null=True, blank=True)
    zipcode = models.CharField("Zip/Postal Code", max_length=10)
    city = models.CharField("City", max_length=100)
    country = models.CharField("Country", max_length=100, choices=COUNTRIES)


class CompanyEmployee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
