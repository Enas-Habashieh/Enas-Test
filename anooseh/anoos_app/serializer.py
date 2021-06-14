from rest_framework import serializers

from anoos_app.models import EnasFriends, Country, Names


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnasFriends
        fields = '__all__'


class CounrtrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class NamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = '__all__'
