from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DeleteView
from .models import Household, Personal
from .forms import HouseholdForm, PersonalForm
from .resources import PersonalResource, HouseholdResource
from tablib import Dataset
import logging
from django.contrib import messages
import csv, io

from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.views import APIView
import json
import openpyxl
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from openpyxl import workbook
import pyexcel as pe
import django_excel as excel
import pandas as pd
from datetime import datetime
from django.forms.models import model_to_dict
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
# Create your views here.
logger = logging.getLogger(__name__)


class add_Household(SuccessMessageMixin, CreateView):
    template_name='smartprofile/add_Household.html'
    form_class =HouseholdForm
    success_url='/smartprofile/hhdetail/{KEY}'
    def from_valid(self, form):
        return super().from_valid(form)
    def get_success_message(self, cleaned_data):
        return "Household Data Successfully Added Now Add personal to this household"

class add_Personal(SuccessMessageMixin, CreateView):
    template_name='smartprofile/add_Personal.html'
    form_class =PersonalForm
    success_url='/smartprofile/hhdetail/{PARENT_KEY_id}'
    def get_context_data(self, **kwargs):
        """ Get context variables for rendering the template. """
        context=super().get_context_data(**kwargs)
        household = get_object_or_404(Household, pk=self.kwargs['pk'])
        Person=household.personal_set.all()
        context['household']=household
        context['Personal']=Person
        return context
    def form_valid(self, form):
        """ Save the form instance. """
        household = get_object_or_404(Household, pk=self.kwargs['pk'])
        form.instance.PARENT_KEY = household
        return super().form_valid(form)
    def get_success_message(self, cleaned_data):
        return "Personal Data Successfully Added to this household"
class personalupdate(SuccessMessageMixin, UpdateView):
    model=Personal
    template_name='smartprofile/personalupdate.html'
    form_class =PersonalForm
    success_url='/smartprofile/personaldetail/{id}'
    def get_context_data(self, **kwargs):
        """ Get context variables for rendering the template. """
        context=super().get_context_data(**kwargs)
        Personal_object = get_object_or_404(Personal, pk=self.kwargs['pk'])
        hh_key=Personal_object.PARENT_KEY.KEY
        household = get_object_or_404(Household, pk=hh_key)
        context['household']=household
        context['Personal']=Personal_object
        return context
    def get_success_message(self, cleaned_data):
        return "Personal Data Successfully Added to this household"

class personaldelete(SuccessMessageMixin, DeleteView):

    model=Personal
    success_url='/smartprofile/hhdetail/{PARENT_KEY_id}'
    def get_context_data(self, **kwargs):
        """ Get context variables for rendering the template. """
        context=super().get_context_data(**kwargs)
        Personal_object = get_object_or_404(Personal, pk=self.kwargs['pk'])
        hh_key=Personal_object.PARENT_KEY.KEY
        household = get_object_or_404(Household, pk=hh_key)
        context['household']=household
        context['Personal']=Personal_object
        return context
    def get_success_message(self, cleaned_data):
        return "Personal Data Successfully Deleted to this household"

def map(request):
    return render(request, 'smartprofile/map.html', { 'household': "household",
    'nbar':"Map"})

def index(request):
    model = Household
    #field_names = model._meta.get_fields()
    household = model.objects.all()
    columns=[]
    header=model._meta.get_fields()
    for h in header:
        if(h.name != "personal"):
            columns.append(h.name)
    return render(request, 'smartprofile/index.html', { 'household': household,
    'nbar':"Household",'columns1':columns,
    })


def personalList(request):
    Personal_all=Personal.objects.all()
    return render(request,'smartprofile/personalList.html',{'Personal':Personal_all,
    'nbar':"Personal"})

def HHDetailView(request, pk):
    iteam=get_object_or_404(Household,pk=pk)
    form=HouseholdForm(instance=iteam)
    return render(request,'smartprofile/hhdetail.html',{
    'household':iteam,
    'form':form,
    'nbar':"Household"
    })
class householdupdate(SuccessMessageMixin, UpdateView):
    model=Household
    template_name='smartprofile/householdupdate.html'
    form_class =HouseholdForm
    success_url='/smartprofile/hhdetail/{KEY}'
    def get_context_data(self, **kwargs):
        """ Get context variables for rendering the template. """
        context=super().get_context_data(**kwargs)
        household = get_object_or_404(Household, pk=self.kwargs['pk'])
        context['household']=household

        return context
    def get_success_message(self, cleaned_data):
        return "Household Data Successfully UpdateView"

class householddelete(SuccessMessageMixin, DeleteView):
    model=Household
    success_url='/smartprofile/'

    def get_success_message(self, cleaned_data):
        return "Household Data Successfully Deleted."

def personaldetail(request, pk):
    Personal_object=get_object_or_404(Personal,pk=pk)
    HH_Key=Personal_object.PARENT_KEY.KEY
    Household_Object=get_object_or_404(Household,pk=HH_Key)
    form=PersonalForm(instance=Personal_object)
    return render(request,'smartprofile/personaldetail.html',{
    'form':form,
    'household':Household_Object,
    'Personal':Personal_object
    })
def export(request):
    if request.method == 'POST':
        # Get selected option from form
        dataset = request.POST['dataset']
        file_format = request.POST['file-format']
        personal_resource = PersonalResource()
        household_resource=HouseholdResource()
        personal_dataset = personal_resource.export()
        household_dataset = household_resource.export()
        if file_format == 'CSV':
            if dataset=='Personal':
                response = HttpResponse(personal_dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="personal_data.csv"'
                return response
            elif dataset=='Household':
                response = HttpResponse(household_dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="Household_data.csv"'
                return response
        elif file_format == 'JSON':
            if dataset=='Personal':
                response = HttpResponse(personal_dataset.json, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="personal_data.json"'
                return response
            elif dataset=='Household':
                response = HttpResponse(household_dataset.json, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="Household_data.json"'
                return response
        elif file_format == 'XLS (Excel)':
            if dataset=='Personal':
                response = HttpResponse(personal_dataset.xls, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="personal_data.xls"'
                return response
            elif dataset=='Household':
                response = HttpResponse(household_dataset.xls, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="Household_data.xls"'
                return response

    return render(request, 'smartprofile/export.html')
def importData (request):
    if request.method == 'POST' and bool(request.FILES.get('filepath', False)) == True :
        # Get selected option from form
        import_file=request.FILES['importData']

        if (str(import_file).split('.')[-1] == "csv"):
            logger.error("You are Here in CSV Section %s" % import_file)
            data = import_file.read()
            logger.error(data)

        elif (str(import_file).split('.')[-1] == "xls"):
            logger.error("You are Here in xlsx_get Section %s" % import_file)
            data=xls_get(import_file)
            sheets=pe.get_book(import_file)
            logger.error(sheets)
        elif (str(import_file).split('.')[-1] == "xlsx"):

            logger.error("You are Here in XLSX Section '{0}' , '{1}'".format(import_file, a))

            # import_file.save_book_to_database(
            # models=[household],
            # initializers=None,
            # mapdicts=None
            # )
            data=xlsx_get(import_file)
            sheet= import_file.get_records()
            TR=len(sheet)
            i=0
            j=0
            # dicta={'Ward':10,'Tol':"Taukhel"}
            # a=Household(**dicta)
            # a.save()
            for r in sheet:
                hh={}
                record=dict(r)
                record['SubmissionDate']=datetime.strptime(record['SubmissionDate'], '%m/%d/%Y %H:%M')
                record['start']=datetime.strptime(record['start'], '%m/%d/%Y %H:%M')
                record['end']=datetime.strptime(record['end'], '%m/%d/%Y %H:%M')
                record['HouseCode']=str(record['HouseCode'])
                record['Funcational_Type']=str(record['Funcational_Type'])
                c=Household.objects.filter(KEY=record['KEY'])
                # logger.error(c.count())
                if(c.count()==0):
                    logger.error(record['KEY'])
                    m=Household(**record)
                    m.save()
                    # logger.error(m)
                    i+=1
                elif(c.count()==1):
                    j+=1
                logger.error("{3} out of {0} data processed of which {1} Data added and {2} data already Exit".format(TR,i,j,i+j))

            return render(request, 'smartprofile/import.html',{'nbar':"importData",'Massage':str(j)+" records Successpully Uploaded"})

    elif bool(request.FILES.get('filepath', False)) == False :
        return render(request, 'smartprofile/import.html',{'nbar':"importData", 'Massage':"File is not Choosen"})
    return render(request, 'smartprofile/import.html',{'nbar':"importData"})
class ParseExcel(APIView):
    def post(self, request, format=None):
        try:
            excel_file = request.FILES['importData']
        except MultiValueDictKeyError:
            return redirect('smartprofile/import.html')
        if (str(excel_file).split('.')[-1] == "xls"):
            data = xls_get(excel_file)
        elif (str(excel_file).split('.')[-1] == "xlsx"):
            data = (excel_file)
        else:
            return redirect('smartprofile/import.html')
        logger.error(data)
def housedata(request) :
    model = Household

    columns=[]
    header=model._meta.get_fields()
    for h in header:
        if(h.name != "personal"):
            columns.append(h.name)
    return render(request,'smartprofile/housedata.html',{'columns1':columns})


class HouseholdListJson(BaseDatatableView):
    # The model we're going to show
    model = Household

    columns=[]
    header=model._meta.get_fields()
    for h in header:
        if(h.name != "personal"):
            columns.append(h.name)

    # The model we're going to show
    # define the columns that will be returned

    # define column names that will be used in sorting
        # order is important and should be same as order of columns
        # displayed by datatables. For non sortable columns use empty
        # value like ''
    order_columns =  columns
    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
        # and make it return huge amount of data
    # max_display_length = 500
