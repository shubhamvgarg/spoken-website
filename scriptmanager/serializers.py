from creation.models import ContributorRole, FossCategory, Language,TutorialDetail
from rest_framework import serializers
from .models import Scripts, ScriptDetails
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class FossCategorySerializer(serializers.ModelSerializer):
  name = serializers.CharField(source='foss')
  class Meta:
    model=FossCategory
    fields=('id','name')

class LanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model=Language
    fields=('id','name')

class ContributorRoleSerializer(serializers.ModelSerializer):
    foss_category=FossCategorySerializer(read_only=True)
    language=LanguageSerializer(read_only=True)
    user=serializers.CharField()
    class Meta:
      model = ContributorRole
      fields = ('foss_category','language','user', 'status')


class TutorialDetailSerializer(serializers.ModelSerializer):
    class Meta:
      model=TutorialDetail
      fields=('id','foss','tutorial','level','order','user','created','updated')


class ScriptsDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model=ScriptDetails
    fields=('id','cue','narration','order')

class ScriptsSerializer(serializers.ModelSerializer):
  details=ScriptsDetailSerializer(many=True)

  class Meta:
    model=Scripts
    fields=('details',)

 