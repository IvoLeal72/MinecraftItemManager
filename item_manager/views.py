from django.db import transaction
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from . import models


# Create your views here.

class UpdateItems(APIView):

    @transaction.atomic
    def post(self, request: Request):
        return Response()
        models.Item.objects.update(count=0)
        items = [models.Item(id=name, count=count) for name, count in request.data.items()]
        models.Item.objects.bulk_create(items, update_conflicts=True, update_fields=['count'], unique_fields=['id'])
        return Response()
