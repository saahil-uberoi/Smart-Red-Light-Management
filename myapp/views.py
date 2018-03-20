# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Mapp, Crossing1
import json
from import_files import *
from django.shortcuts import render, redirect
from forms import DataForm
from import_files import *
from key import get_your_own_key, get_your_own_key1
import json
# Create your views here.

IMAGE_URL = []


def display(request):
    if request.method == 'GET':
        form = DataForm(request.GET)
        if form.is_valid():
            cam1 = form.cleaned_data['cam1']
            cam2 = form.cleaned_data['cam2']
            cam3 = form.cleaned_data['cam3']
            cam4 = form.cleaned_data['cam4']
            print cam1
            # stray(cam1, cam2, cam3, cam4)
            result = api_call(cam1, cam2, cam3, cam4)
            print result
            return render(request, 'disp.html', {'cam1':cam1, 'cam2':cam2 , 'cam3':cam3, 'cam4':cam4, 'result1':result[0],
                                    'result2':result[1], 'result3':result[2], 'result4':result[3]})
        else:
            return render(request, 'data.html')


def api_call(cam1, cam2, cam3, cam4):
    app = image_analyzer(api_key=get_your_own_key)
    model = app.models.get('traffic density')
    images = [cam1, cam2, cam3, cam4]
    emergency = {}
    low = {}
    high = {}
    n = 0
    for i in range(0, len(images)):
        image = Image(url=images[i])
        data = model.predict([image])
        with open('repo_data.json', 'w') as outfile:
            json.dump(data, outfile)
        print data
        print "\n\n"
        x = data['outputs'][0]['data']['concepts'][0]['name']
        y = data['outputs'][0]['data']['concepts'][0]['value']
        c = "cam" + str(i + 1)
        if x == 'ambulance' or x == 'fire':
            emergency[c] = y
        elif x == 'low density':
            low[c] = y
        elif x == 'high density':
            high[c] = y
    print emergency
    print high
    print low
    flag = 0
    str1 = ''
    str2 = []
    if emergency:
        max_value = max(emergency.itervalues())
        z = [k for k in emergency if emergency[k] == max_value]
        del emergency[''.join(z)]
        # print ''.join(z) + "  is green for 20 seconds and then red for 60 seconds"
        str1 = ''.join(z) + "  is green for 20 seconds and then red for 60 seconds"
        str2.append(str1)
        flag = 1
        for l in range(0, len(emergency)):
            max_value1 = max(emergency.itervalues())
            z1 = [k1 for k1 in emergency if emergency[k1] == max_value1]
            n = n + 20
            # print ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str2.append(str1)
            del emergency[''.join(z1)]
    if high:
        max_value = max(high.itervalues())
        z = [k for k in high if high[k] == max_value]
        del high[''.join(z)]
        if flag == 1:
            n = n + 20
            # print ''.join(z) +  " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = ''.join(z) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str2.append(str1)
        else:
            flag = 1
            str1 = ''.join(z) + "  is green for 20 seconds and then red for 60 seconds"
            str2.append(str1)
        for l in range(0, len(high)):
            max_value1 = max(high.itervalues())
            z1 = [k1 for k1 in high if high[k1] == max_value1]
            n = n + 20
            # print ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str2.append(str1)
            del high[''.join(z1)]
    if low:
        min_value = min(low.itervalues())
        z = [k for k in low if low[k] == min_value]
        del low[''.join(z)]
        if flag == 1:
            n = n + 20
            # print ''.join(z) +  " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = ''.join(z) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str2.append(str1)
        else:
            str1 = ''.join(z) + "  is green for 20 seconds and then red for 60 seconds"
            str2.append(str1)
        for l in range(0, len(low)):
            min_value1 = min(low.itervalues())
            z1 = [k1 for k1 in low if low[k1] == min_value1]
            n = n + 20
            # print ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str1 = ''.join(z1) + " is red for " + str(n) + " seconds and then green for 20 seconds"
            str2.append(str1)
            del low[''.join(z1)]

    return str2

#
# def stray(cam1,cam2,cam3,cam4):
#    app1 = image_analyzer(api_key=get_your_own_key1)
#    app1.inputs.delete_all()
#    images = [cam1, cam2, cam3, cam4]
#    for i in range(0, len(images)):
#        app1.inputs.create_image_from_url(images[i])
#        data1 = app1.inputs.search_by_predicted_concepts(concept='animal')
#        if data1:
#            print "cam" + str(i+1) + ": Animal Detect"
#        else:
#            print "cam" + str(i + 1) + ": No Animal Detect"
#
