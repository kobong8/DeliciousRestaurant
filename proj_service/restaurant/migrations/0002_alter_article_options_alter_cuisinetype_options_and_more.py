# Generated by Django 5.0.6 on 2025-02-15 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '칼럼', 'verbose_name_plural': '칼럼들'},
        ),
        migrations.AlterModelOptions(
            name='cuisinetype',
            options={'verbose_name': '음식 종류', 'verbose_name_plural': '음식 종류'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': '음식점', 'verbose_name_plural': '음식점들'},
        ),
        migrations.AlterModelOptions(
            name='restaurantcategory',
            options={'verbose_name': '가게 카테고리', 'verbose_name_plural': '가게 카테고리'},
        ),
        migrations.AlterModelOptions(
            name='restaurantimage',
            options={'verbose_name': '가게 이미지', 'verbose_name_plural': '가게 이미지'},
        ),
        migrations.AlterModelOptions(
            name='restaurantmenu',
            options={'verbose_name': '가게 메뉴', 'verbose_name_plural': '가게 메뉴'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at'], 'verbose_name': '리뷰', 'verbose_name_plural': '리뷰들'},
        ),
        migrations.AlterModelOptions(
            name='reviewimage',
            options={'verbose_name': '리뷰이미지', 'verbose_name_plural': '리뷰이미지'},
        ),
        migrations.AlterModelOptions(
            name='socialchannel',
            options={'verbose_name': '소셜채널', 'verbose_name_plural': '소셜채널'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '태그', 'verbose_name_plural': '태그들'},
        ),
    ]
