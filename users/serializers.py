from rest_framework import serializers
from .models import webhook_logs

class WebhookLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = webhook_logs
        fields = '__all__'