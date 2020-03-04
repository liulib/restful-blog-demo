from .models import Category, Articles, Tag
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        # fields = "__all__"
        fields = ('id', 'title', 'brief', 'content', 'update_time', 'recommend', 'read_nums', 'fav_nums', 'category', 'tag', 'author')


