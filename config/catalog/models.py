from django.db import models

# Create your models here.
# Name,
# description,
# image (preview),
# category,
# purchase price,
# date of creation,
# last modified date.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.BooleanField(default=True, verbose_name='created')

    def __str__(self):
        return self.title
