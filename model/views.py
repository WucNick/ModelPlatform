from django.shortcuts import render
from django.http import HttpResponse


def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息1。。。")

def listorders1(request):
    return HttpResponse("下面是系统中所有的订单信息2。。。")
