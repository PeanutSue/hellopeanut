# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
# from django.http import JsonResponse

from home_application.models import MultRecord


def home(request):
    """
    首页
    """
    all_record = MultRecord.objects.all()
    ctx = {
        'all_record': all_record
    }
    return render_mako_context(request, '/home_application/home.html', ctx)


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def hellopeanut(request):
    """
    hellopeanut
    """
    return render_mako_context(request, '/home_application/hellopeanut.html')
