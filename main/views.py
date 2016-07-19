# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import stuffs_sort
from django.template import RequestContext
from django.http import HttpResponse
import json

# Create your views here.

korean_category_names = ['의류', '패션잡화', '미용', '출산/유아', '모바일', '컴퓨터', '카메라', '영상기기', '음악/악기', '게임', '스포츠/취미', '여행',
                         '생활용품', '사무용품', '가구/인테리어', '미술/예술', '도서/참고서', '차/오토바이/자전거', '기타']


def main(request):
    stuffs = stuffs_sort.objects.all()
    return render_to_response('index.html', RequestContext(request, {"stuffs": stuffs,
                                                                     'korean_category_names': korean_category_names}))

def filtered_userstuff_data(request):

    category = request.GET['category']

    stuffs = stuffs_sort.objects.filter(category=category)
    json_stuff = []
    for stuff in stuffs:
        json_stuff.append({'name':stuff.name})
    return HttpResponse(json.dumps(json_stuff, indent=4, sort_keys=True), content_type="application/json")

