from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='static/default_avatar.png')


class Author(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='brand/', blank=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=256)
    alias = models.SlugField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='тег')
    image = models.ImageField(upload_to='product/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField()
    slug = models.SlugField()

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name

    def reviews(self):
        return self.reviews.all()



class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    created_date = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'




# class Order
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
#     created_date = models.DateTimeField(auto_now_add=True)
#     product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)






# class Shipping

