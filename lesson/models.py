from django.db import models


# Modelクラスの継承
class Book(models.Model):
    isbn = models.CharField(
        verbose_name='ISBNコード',
        max_length=20
    )
    title = models.CharField(
        verbose_name='書名',
        max_length=100
    )
    price = models.IntegerField(
        verbose_name='価格',
        default=0
    )
    publisher = models.CharField(
        verbose_name='出版社',
        max_length=50,
        choices=[
            ('A', 'AAA社'),
            ('B', 'BBB社'),
            ('C', 'CCC社'),
        ],
    )
    published = models.DateField(
        verbose_name='刊行日'
    )

    # モデルの文字列表現
    def __str__(self):
        return f'{self.title}({self.publisher}/{self.price}円)'
