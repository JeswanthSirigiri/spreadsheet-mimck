from rest_framework import serializers
from .models import Spreadsheetapp

class SpreadsheetappSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(required=False)
    class Meta:
        model = Spreadsheetapp
        fields = ['id', 'name', 'data']
        depth = 1
