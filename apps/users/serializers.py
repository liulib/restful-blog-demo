from operations.models import Comments
from rest_framework import serializers


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"



