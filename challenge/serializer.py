from rest_framework import serializers
from challenge.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    def validate_titulo(self, titulo):
        if len(titulo)<100:
            raise serializers.ValidationError("Digite um título válido! Por favor, não coloque números")
        return titulo
    def validate_description(self, descricao):
        if len(descricao)<500:
            raise serializers.ValidationError("Digite uma descrição válida!")
        return descricao