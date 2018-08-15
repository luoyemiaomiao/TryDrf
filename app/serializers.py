from rest_framework import serializers
from app import models
# class PublisherSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#     def create(self,validated_data):
#         # validated_data新的数据
#         return models.Publisher.objects.create(**validated_data)
#     def update(self, instance, validated_data):#更新
#         instance.name = validated_data.get('name',instance.name)
#         instance.address = validated_data.get('address',instance.address)
#         instance.save()
#         return instance
# ModelSerializer继承model
class PublisherSerializer(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model = models.Publisher
        fields = (
            'id','name','address','operator'
        )
class BookSerializer(serializers.HyperlinkedModelSerializer):
    # publisher = serializers.StringRelatedField(source='publisher.name')#关系到出版社的名字
    class Meta:
        model = models.Book
        fields = (
            'id','title','publisher'
        )