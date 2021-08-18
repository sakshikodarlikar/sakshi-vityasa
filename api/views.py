# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse
import json
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from rest_framework.response import Response
from .models import *
import datetime
from itertools import combinations

# POST data in raw text format
@api_view(('POST',))
def task1 (request):
    data = request.body.decode('UTF-8')
    
    data = eval(data)
    x=[]
    valid_entries = 0
    invalid_entries = 0
    for i in data :
        try :
            print (i)
            i = int(i)
            if i>0:
                x.append(i)
                valid_entries += 1
        except :
            invalid_entries += 1
    print(x)
    dict = { 'valid_entries': valid_entries,
             'invalid_entries': invalid_entries,
             'min': min(x),
             'max': max(x),
             'average': sum(x)/len(x),
             }
    return Response(dict, status=status.HTTP_200_OK)  

def delete_all ():
    today_date = datetime.date.today()
    slot_list = Slot.objects.all()
    for slot in slot_list:
        if slot.slot_date != today_date:
            slot.delete()


@api_view(('GET','POST'))
def task2_booking(request):
    delete_all()
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        if data['slot'] < 24  and data['slot'] >= 0:
            try :
                slot = Slot.objects.get(slot_id=data['slot']) 
            except :
                slot = Slot.objects.create(slot_id=data['slot'],slot_date=datetime.date.today())
                slot.save()
            
            if slot.slot_1 == '':
                slot.slot_1 = data['name']
                slot.date = datetime.date.today()
                slot.save()
            elif slot.slot_2 == '':
                slot.slot_2 = data['name']
                slot.date = datetime.date.today()
                slot.save()
            else :
                return Response({"status":f"slot full, unable to save booking for {data['name']} in slot{data['slot']}"},status=status.HTTP_409_CONFLICT)
            return Response({"status": "confirmed"},status=status.HTTP_200_OK)
        else :
            return Response({"status":f"slot number must be between 1 and 12"},status=status.HTTP_400_BAD_REQUEST)    
        

    elif request.method == 'GET':
        slots = Slot.objects.all()
        slot_list = []
        lis = {}
        for slot in slots:
            if slot.slot_1 == '' and slot.slot_2 == '':
                slot.delete()
            else: 
                lis = { 'slot': slot.slot_id,'name':[slot.slot_1,slot.slot_2] }
                slot_list.append(lis) 
        return Response(slot_list,status=status.HTTP_200_OK)


@api_view(('POST',))
def task2_cancel(request):
    delete_all()
    data = json.loads(request.body.decode("utf-8"))
    slot = Slot.objects.get(slot_id=data['slot'])
    print (slot.slot_1,data['name'])
    if slot.slot_1 == data['name']:
        slot.slot_1 = ''
        slot.save()
    elif slot.slot_2 == data['name']:
        slot.slot_2 = ''
        slot.save()
    else :
        return Response({"status":f"no booking for the name {data['name']} in slot {data['slot']}"},status=status.HTTP_409_CONFLICT)
    return Response({"status": f"canceled booking for {data['name']} in slot {data['slot']}"},status=status.HTTP_200_OK)

### CODE FOR Checking square 
class Point:
     
    # Structure of a point in 2D space
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# A utility function to find square of
# distance from point 'p' to point 'q'
def distSq(p, q):
    return (p.x - q.x) * (p.x - q.x) +\
           (p.y - q.y) * (p.y - q.y)
 
# This function returns true if (p1, p2, p3, p4)
# form a square, otherwise false
def isSquare(p1, p2, p3, p4):
 
    d2 = distSq(p1, p2) # from p1 to p2
    d3 = distSq(p1, p3) # from p1 to p3
    d4 = distSq(p1, p4) # from p1 to p4
 
    if d2 == 0 or d3 == 0 or d4 == 0:   
        return False
 
    # If lengths if (p1, p2) and (p1, p3) are same, then
    # following conditions must be met to form a square.
    # 1) Square of length of (p1, p4) is same as twice
    # the square of (p1, p2)
    # 2) Square of length of (p2, p3) is same
    # as twice the square of (p2, p4)
 
    if d2 == d3 and 2 * d2 == d4 and \
                    2 * distSq(p2, p4) == distSq(p2, p3):
        return True
 
    # The below two cases are similar to above case
    if d3 == d4 and 2 * d3 == d2 and \
                    2 * distSq(p3, p2) == distSq(p3, p4):
        return True
 
    if d2 == d4 and 2 * d2 == d3 and \
                    2 * distSq(p2, p3) == distSq(p2, p4):
        return True
 
    return False

@api_view(('POST',))
def task3 (request):
    data = json.loads(request.body.decode("utf-8"))
    saved_list = []
    if not 'points' in request.session or not request.session['points']:
        request.session['points'] = [[data['x'],data['y']]]
        print(request.session['points'])
    else:
        saved_list = request.session['points']
        saved_list.append([data['x'],data['y']])
        request.session['points'] = saved_list
    if len(request.session['points']) > 3:
        b = list(combinations(request.session['points'],4))
        for i in b :
            i=list(i)
            if isSquare(Point(i[0][0],i[0][1]), Point(i[1][0],i[1][1]), Point(i[2][0],i[2][1]), Point(i[3][0],i[3][1])):
                request.session.flush()
                return Response ({"status":f"Success {i}"},status=status.HTTP_200_OK)
        return Response({"status":"accepted"},status=status.HTTP_200_OK)
    else :
        return Response({"status":"accepted"},status=status.HTTP_200_OK)