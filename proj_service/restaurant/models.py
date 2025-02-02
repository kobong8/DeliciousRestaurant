from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    preview_image = models.ImageField(upload_to="article", null=True, blank=True)
    content = models.TextField()
    show_at_index = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Restaurant(models.Model):
    name = models.CharField("이름", max_length=100, db_index=True)
    branch_name = models.CharField(
        "지점", max_length=100, db_index=True, null=True, blank=True
    )
    preview_image = models.ImageField(upload_to="article", null=True, blank=True)
    description = models.TextField("설명", null=True, blank=True)
    address = models.CharField("주소", max_length=255, db_index=True)
    feature = models.CharField("특징", max_length=255)
    is_closed = models.BooleanField("폐업 여부", default=False)
    latitude = models.DecimalField(
        "위도",
        max_digits=16,
        decimal_places=12,
        db_index=True,
        default="0.0000",
    )
    longitude = models.DecimalField(
        "경도",
        max_digits=16,
        decimal_places=12,
        db_index=True,
        default="0.0000",
    )
    phone = models.CharField(
        "전화번호", max_length=16, help_text="E.164 포맷", blank=True, null=True
    )
    rating = models.DecimalField("평점", max_digits=3, decimal_places=2, default="0.0")
    rating_count = models.PositiveIntegerField("평가수", default=0)
    start_time = models.TimeField("영업 시작 시간", null=True, blank=True)
    end_time = models.TimeField("영업 종료 시간", null=True, blank=True)
    last_order_time = models.TimeField("라스트 오더 시간", null=True, blank=True)
    category = models.ForeignKey(
        "RestaurantCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    tags = models.ManyToManyField("Tag", blank=True)
