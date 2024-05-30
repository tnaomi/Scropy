from rest_framework import serializers
from api.models import Crops, Countries, Zone

class CropsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    genus = serializers.CharField()
    description = serializers.CharField()
    matures_in = serializers.FloatField()
    bi_annual = serializers.BooleanField()
    suitable_zone = serializers.ModelField(Zone)
    consumed_in = serializers.ModelField(Countries)

    def create(self, validated_data):
        """ Create a crop instance given crop data """
        return Crops.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update Crop object """
        instance.name = validated_data.get('name', instance.name)
        instance.genus = validated_data.get('genus', instance.genus)
        instance.description = validated_data.get('description', instance.description)
        instance.matures_in = validated_data.get('matures_in', instance.matures_in)
        instance.bi_annual = validated_data.get('bi_annual', instance.bi_annual)
        instance.suitable_zone = validated_data('suitable_zone', instance.suitable_zone)
        instance.consumed_in = validated_data('consumed_in', instance.consumed_in)
        instance.save()
        return Crops.objects.update(**instance, **validated_data)

class ZoneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.IntegerField(read_only=True)
    annual_rainfall = serializers.FloatField()
    avg_temp = serializers.FloatField()
    districts = serializers.ModelField(Zone)

    def create(self, validated_data):
        """ Create a Zone object """
        return Zone.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update a Zone """
        instance.name = validated_data.get('name', instance.name)
        instance.annual_rainfall = validated_data.get('annual_rainfall', instance.annual_rainfall)
        instance.avg_temp = validated_data.get('avg_temp', instance.avg_temp)
        instance.districts = validated_data.get('districts', instance.districts)
        instance.save()
        return Zone.objects.update(**instance, **validated_data)

class CountriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    region = serializers.DictField()

    def create(self, validated_data):
        """ Create Countries object """
        return Countries.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update a Countries object """
        instance.name = validated_data.get('name', instance.name)
        instance.region = validated_data.get('region', instance.region)
        instance.save()
        return Countries.objects.update(**instance, **validated_data)