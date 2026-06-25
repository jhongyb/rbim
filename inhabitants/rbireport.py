import io,os
from django.http import FileResponse,HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.staticfiles import finders
from reportlab.lib.pagesizes import A4
from .models import Inhabitants,Households
from django.db.models import F,Value
import datetime 
import pdfkit
from django.template.loader import render_to_string
from django.db.models.functions import Substr,StrIndex,ExtractYear
from django.utils import timezone

now=timezone.now()

def centerstring(text,tv,tx,p):
        tw=p.stringWidth(text)
        pw=tx
        return p.drawString((pw-tw)/2,tv,text)

@login_required()
def rbiformb(request,pk):
    data=Inhabitants.objects.get(id=pk)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setTitle('RBI FORM B - ' + pk)
    fn=f'{data.lastname}-{data.firstname}-{data.middlename}-{pk}'
    bg = finders.find('img/formb.jpg')
    p.drawImage(bg,0,0,width=A4[0],height=A4[1])
    p.setFontSize(10)
    p.drawString(155,752, "REGION XII")
    p.drawString(155,731, "SULTAN KUDARAT")

    p.drawString(445,752, "BAGUMBAYAN")
    p.drawString(445,731, str(data.hh.barangay.name))
    centerstring(str(data.philsysno),655,260,p)
    centerstring(str(data.hh.household_no),125,460,p)
    centerstring(str(data.lastname),610,220,p)
    centerstring(str(data.extname),610,420,p)
    centerstring(str(data.firstname),610,630,p)
    centerstring(str(data.middlename),610,950,p)
    centerstring(str(data.birthday.strftime('%m/%d/%Y')),570,191,p)
    p.setFontSize(9)
    bp=f"{data.bpcity}, {data.bpprovince}"
    centerstring(str(bp),570,450,p)
    p.setFontSize(10)
    def jstring(text):
          data=str(text).split()[1:]
          return " ".join(data)
    centerstring(jstring(data.sex),570,650,p)
    centerstring(jstring(data.maritalstatus),570,800,p)
    p.setFontSize(9)
    centerstring(str(data.religion),570,1000,p)
    centerstring(str(data.hh.address),530,460,p)
    p.setFontSize(10)
    centerstring(jstring(data.nationality),530,990,p)
    centerstring(str(data.occupation),486,260,p)
    centerstring(str(data.contactno),486,630,p)
    centerstring(str(data.email),486,955,p)
    def mark(txt):
          num=str(txt).split()[0]
          return num
    #college
    centerstring('X' if mark(data.highesteducation)=='12' else '',445,755,p)
    centerstring('X' if mark(data.highesteducation)=='12' else '',423,550,p)#graduate

    centerstring('X' if mark(data.highesteducation)=='11' else '',445,755,p)
    centerstring('X' if mark(data.highesteducation)=='11' else '',423,673,p)#undergraduate

    #elementary
    centerstring('X' if mark(data.highesteducation)=='2' else '',445,483,p) #
    centerstring('X' if mark(data.highesteducation)=='2' else '',423,673,p) #undergraduate

    centerstring('X' if mark(data.highesteducation)=='3' else '',445,483,p) #
    centerstring('X' if mark(data.highesteducation)=='3' else '',423,550,p)#graduate

    #highschool

    centerstring('X' if mark(data.highesteducation)=='4' else '',445,620,p) #
    centerstring('X' if mark(data.highesteducation)=='4' else '',423,673,p) #undergraduate

    centerstring('X' if mark(data.highesteducation)=='5' else '',445,620,p) #
    centerstring('X' if mark(data.highesteducation)=='5' else '',423,550,p)#graduate
  
    #postgrad
    centerstring('X' if mark(data.highesteducation)=='13' else '',445,865,p) #
#     centerstring('X' if mark(data.highesteducation)=='13' else '',423,550,p)#graduate

    centerstring('X' if mark(data.highesteducation)=='10' else '',445,990,p) #
    centerstring(f'{data.firstname} {data.middlename} {data.lastname} {data.extname}',320,850,p) #
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename=f'{fn}.pdf')

def long_landscape(html):
       options = {
          'page-size':'A4',
          'orientation':'landscape',
          'encoding': "UTF-8",
            'margin-top': '0.5in',
            'margin-right': '0.2in',
            'margin-bottom': '0.3in',
            'margin-left': '0.2in',
            'encoding': "UTF-8",
            'enable-local-file-access': True,
            'footer-right':'Page  [PAGE] of [topage]',
            'title':"ITEM REPORT",
            'footer-Font-size':'8',
       }
       config =pdfkit.configuration(wkhtmltopdf='./static/wkhtmltopdf') 
       pdf = pdfkit.from_string(html, False, configuration=config, 
       options=options)
       response = HttpResponse(pdf, content_type='application/pdf')
       response['Content-Disposition'] = 'inline; filename="{}_{}.pdf"'.format('Report','12')
       return response

@login_required()
def rbiforma(request,pk):
      
      data=Inhabitants.objects.filter(hh=pk).annotate(
            gender=F('sex__description'),civil_status=F('maritalstatus__description')
            ,citizenship=F('nationality__description'),age=now.year-ExtractYear('birthday'))
      house=Households.objects.get(id=pk)
      context={'data':data,'house':house}
      html=render_to_string('reports/rbiforma.html',context)
      return long_landscape(html=html)