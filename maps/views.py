from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
import os
import json

from .models import GeoArea

# Create your views here.

def index(request):
    return HttpResponse("nothing is finished")


def demo(request):
    return render(request, 'maps/demo.html')


def baidumap(request):
    return render(request, 'maps/baidumap.html')


def heatmap(request):
    return render(request, 'maps/heatmap.html')


def movemap(request):
    return render(request, 'maps/movemap.html')


def area(request, c):
    try:
        area = GeoArea.objects.get(code=c)
        filename = _geojson_filename(area.level, c)
        obj = _load_jsonfile(filename)
    except GeoArea.DoesNotExist:
        raise Http404("Area with code %s cannot be found." % c)
    except:
        raise Http404("Area with code %s JSON file cannot be found" % c)

    return _return_jsonp_response(obj)


def hot_areas(request):
    try:
        areas = GeoArea.objects.filter(is_hot=1)
        rt = None
        for area in areas:
            filename = _geojson_filename(area.level, area.code)
            obj = _load_jsonfile(filename)
            if rt is None:
                rt = obj
            else:
                rt['features'] = rt['features'] + obj['features']
    except GeoArea.DoesNotExist:
        raise Http404("Hot areas cannot be found.")
    except Exception as e:
        raise Http404("Hot areas JSON file cannot be found")

    return _return_jsonp_response(rt)


def hot_area_names(request):
    try:
        areas = GeoArea.objects.filter(is_hot=1)
        rt = {'cities': []}
        for area in areas:
            city = {'name': area.name}
            city['location'] = {
                'latitude': area.cp_latitude,
                'longitude': area.cp_longitude,
            }
            rt['cities'].append(city)
    except Exception as e:
        raise Http404("Hot areas cannot be found")

    return _return_jsonp_response(rt)


def _geojson_filename(level, code):
    code = int(code)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if level == 1:
        filename = base_dir + "/china-cities/datas/%d.json" % code
    elif level == 2:
        p = (code // 10000) * 10000
        filename = base_dir + "/china-cities/datas/%d/%d.json" % (p, code)
    else:
        filename = ""

    return filename


def _load_jsonfile(filename):
    f = open(filename, encoding='utf-8')
    jsonstr = f.read()
    jsonstr = jsonstr.replace("\ufeff", "")
    f.close()
    return json.loads(jsonstr)


def _return_jsonp_response(obj):
    resp = JsonResponse(obj)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp


