from django.shortcuts import render
from django.views.generic import TemplateView
from random import choice
from urllib import request
import json

url = request.urlopen('https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json')
words = json.loads(url.read())


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        return {'some_data': [choice(words) for i in range(10)]}


class Report(TemplateView):
    template_name = 'main/report.html'
