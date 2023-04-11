import logging,json,datetime,os
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework.response import Response
from django.db import connection, transaction, connections

class Splunk(APIView):
    logger = logging.getLogger("cm")
    #permission_classes = (IsAuthenticated,)
    permission_classes = ()

    def post(self, request, format=None):
        self.logger.info(request.body.decode('utf-8'))
        self.logger.info(request)
        try:
            context = json.loads(request.body.decode('utf-8'))
        except Exception as e:
            self.logger.error(e)

        method = context.get('method')
        if method == "search_all":
            result={"state": "ok", "data": '22'}
            return Response(result, status=200)


