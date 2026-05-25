
import pdfkit
from django.db.models import F,Q,Sum,Func,CharField,IntegerField
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.conf import settings
import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime,time,date


def Report_A4(iid,html,orientation,title):
       aydi=iid
       html=html
       options = {
          'page-size': 'A4',
          'orientation':orientation,
          'encoding': "UTF-8",
            'margin-top': '0.5in',
            'margin-right': '0.2in',
            'margin-bottom': '0.3in',
            'margin-left': '0.2in',
            'encoding': "UTF-8",
            'enable-local-file-access': True,
            'footer-right':'Page  [PAGE] of [topage]',
            'title':title,
            'footer-Font-size':'8',
       }
       config =pdfkit.configuration(wkhtmltopdf='.\static\wkhtmltopdf.exe') 
       pdf = pdfkit.from_string(html, False, configuration=config, 
       options=options)
       response = HttpResponse(pdf, content_type='application/pdf')
       response['Content-Disposition'] = 'inline; filename="'+f"{title}_{iid}.pdf".format('Report','12')
       return response