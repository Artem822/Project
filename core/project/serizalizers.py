from rest_framework import serializers
from .models import*

class EmployeeSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EducationSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        
class SkipSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Skip
        fields = "__all__"