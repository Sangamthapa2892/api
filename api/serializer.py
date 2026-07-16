from rest_framework import serializers
from .models import Student, Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'




        


    
