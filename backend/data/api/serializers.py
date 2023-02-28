from rest_framework import serializers
from typing import Sequence 

from ..models import URLS 

class URLSSerilizer(serializers.ModelSerializer):
    class Meta:
        model: URLS = URLS
        fields: Sequence[str] = ['visited', "text"]