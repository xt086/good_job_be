from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'number', 'gender', 'age', 'email', 'employee_address', 'personal_introduction', 'level', 'min_salary', 'max_salary', 'major', 'prefer_jobs')
