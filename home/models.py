import os

from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    name = os.getenv('NAME')
