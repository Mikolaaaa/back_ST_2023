from gosuslugi.models import Polzovateli, Uslugi, ZayavkiPolz
from rest_framework import serializers


class PolzovateliSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Polzovateli
        # Поля, которые мы сериализуем
        fields = ["id", "id_request", "username", "manager", "passport", "fio", "snils", "oms", "inn"]

class UslugiSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Uslugi
        # Поля, которые мы сериализуем
        fields = ["id", "name", "description", "document"]

class ZayavkiPolzSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = ZayavkiPolz
        # Поля, которые мы сериализуем
        fields = ["id", "id_user", "id_service", "status", "files"]