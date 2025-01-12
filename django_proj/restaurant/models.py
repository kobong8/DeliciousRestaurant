from django.db import models

class Restaurant(models.Model):
    name = models.CharField("이름", max_length=50, db_index=True)
    category = models.CharField("카테고리", max_length=50, blank=True, null=True)
    address = models.CharField("주소", max_length=255)
    phone = models.CharField("전화번호", max_length=16, help_text="E.164 포맷", db_index=True)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    rating = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"