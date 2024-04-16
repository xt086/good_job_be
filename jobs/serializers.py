from rest_framework import serializers

from .models import Jobs


class JobsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields = ('name', 'expired_time', 'salary', 'description', 'level', 'major')
