# Django Rest Frameworkをインポート
from rest_framework import serializers
# 任意のモデルクラスをインポート
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # 特に指定せず全ての項目をレスポンスする場合
        fields = '__all__'