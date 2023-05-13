import json

from django.shortcuts import render
from rest_framework import viewsets
from gosuslugi.models import Polzovateli, Uslugi, ZayavkiPolz
from gosuslugi.serializers import PolzovateliSerializer, UslugiSerializer, ZayavkiPolzSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse



# Create your views here.
class PolzovateliViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Polzovateli.objects.all().order_by('id')
    serializer_class = PolzovateliSerializer  # Сериализатор для модели

class UslugiViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Uslugi.objects.all().order_by('id')
    serializer_class = UslugiSerializer  # Сериализатор для модели

class ZayavkiPolzViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = ZayavkiPolz.objects.all().order_by('id')
    serializer_class = ZayavkiPolzSerializer  # Сериализатор для модели


@api_view(["POST"])
def create_usluga(request):
    body = json.loads(request.body)
    head = request.headers
    log = head["username"]
    name = body["name"]
    description = body["description"]
    document = body["document"]
    token = head["Authorization"]
    if (log != "undefind") and (token != "undefind"):
        p = Uslugi.objects.create(name=name, description=description, document=document)
        response = Response("{\"status\": \"ok\"}", content_type="json")
        return response
    else:
        return HttpResponse("{\"status\": \"error\", \"error\": \"вы не можете заказать услугу, проверьте введенные "
                            "данные\"}")


@api_view(["POST"])
def create_zayavka(request):
    body = json.loads(request.body)
    head = request.headers
    log = head["username"]
    name = body["name"]
    status = body["status"]
    files = body["files"]
    token = head["Authorization"]
    if (log != "undefind") and (token != "undefind"):
        p = ZayavkiPolz.objects.create(name=name, status=status, files=files)
        response = Response("{\"status\": \"ok\"}", content_type="json")
        return response
    else:
        return HttpResponse("{\"status\": \"error\", \"error\": \"вы не можете заказать услугу, проверьте введенные "
                            "данные\"}")


@api_view(["POST"])
def create_polzovatel(request):
    body = json.loads(request.body)
    head = request.headers
    log = head["username"]
    name = body["name"]
    manager = 0
    passport = body["passport"]
    fio = body["fio"]
    snils = body["snils"]
    oms = body["oms"]
    inn = body["inn"]
    token = head["Authorization"]
    if (log != "undefind") and (token != "undefind"):
        p = Polzovateli.objects.create(name=name, manager=0, passport=passport, fio=fio, snils=snils, oms=oms, inn=inn)
        response = Response("{\"status\": \"ok\"}", content_type="json")
        return response
    else:
        return HttpResponse("{\"status\": \"error\", \"error\": \"вы не можете добавить данные о себе, проверьте "
                            "введенные данные\"}")


@api_view(['DELETE'])
def delPozl(request, id):
    head = request.headers
    log = head["username"]
    token = head["Authorization"]
    if log == "krasava":
        Polzovateli.objects.filter(id=id).delete()
        return HttpResponse('{"status": "ok"')
    else:
        return HttpResponse('{"status": "Access denied"}')


@api_view(['DELETE'])
def delUsl(request, id):
    head = request.headers
    log = head["username"]
    token = head["Authorization"]
    if log == "krasava":
        Uslugi.objects.filter(id=id).delete()
        return HttpResponse('{"status": "ok"')
    else:
        return HttpResponse('{"status": "Access denied"}')


@api_view(['DELETE'])
def delZay(request, id):
    head = request.headers
    log = head["username"]
    token = head["Authorization"]
    if log == "krasava":
        ZayavkiPolz.objects.filter(id=id).delete()
        return HttpResponse('{"status": "ok"')
    else:
        return HttpResponse('{"status": "Access denied"}')


@api_view(['PUT'])
def statusZayChange(request, id):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        head = request.headers
        log = head["username"]
        token = head["Authorization"]
        if log == "krasava":
            status = body["status"]
            zay_by_id = ZayavkiPolz.objects.get(id=id)
            zay_by_id.otsrochka = status
            zay_by_id.save()
            return HttpResponse('{"status": "ok"')
        else:
            return HttpResponse('{"status": "Access denied"}')


@api_view(['PUT'])
def statusZayChangeUser(request, id):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        head = request.headers
        log = head["username"]
        token = head["Authorization"]
        if (log != "undefind") and (token != "undefind"):
            status = body["status"]
            zay_by_id = ZayavkiPolz.objects.get(id=id)
            zay_by_id.otsrochka = status
            zay_by_id.save()
            return HttpResponse('{"status": "ok"')
        else:
            return HttpResponse('{"status": "Access denied"}')


@api_view(['PUT'])
def uslugiChange(request, id):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        head = request.headers
        log = head["username"]
        token = head["Authorization"]
        if log == "krasava":
            name = body["name"]
            description = body["description"]
            document = body["document"]
            uslugi_by_id = Uslugi.objects.get(id=id)
            uslugi_by_id.name = name
            uslugi_by_id.description = description
            uslugi_by_id.document = document
            uslugi_by_id.save()
            return HttpResponse('{"status": "ok"')
        else:
            return HttpResponse('{"status": "Access denied"}')