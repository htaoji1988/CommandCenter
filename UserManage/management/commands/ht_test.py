# -*- coding: utf-8 -*-
# update:2019-07-24 by jihaitao

from django.core.management.base import BaseCommand
from django.db.models import Q
import subprocess
import os, sys
import datetime, time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from django.template import loader
from django.http import StreamingHttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage


class Command(BaseCommand):
    help = "test project"

    def handle(self, *args, **options):
        from UserManage.models import User

        u = User.objects.get(username='jie.liu')
        print(u.token)

