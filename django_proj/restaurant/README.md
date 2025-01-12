- TODO LIST
1. help_text and db_index 의미
```python
phone = models.CharField("전화번호", max_length=16, help_text="E.164 포맷", db_index=True)
```

2. ImageField and blank 의미
```python
image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
```

3. ManyToManyField 의미
```python
keywords = models.ManyToManyField("Keyword", blank=True)
```

4. class Meta 역할
```python
class Meta:
    verbose_name = "가게"
    verbose_name_plural = "가게"
    ordering = ["-rating"]
```