from http.client import HTTPResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
# import pandas as pd
# import os
# from tablib import Dataset
from .models import Voter
# from .resources import VoterResource


# Create your views here.

# def Import_Excel_pandas(request):
    
#     if request.method == 'POST' and request.FILES['myfile']:      
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)              
#         empexceldata = pd.read_excel(filename)        
#         dbframe = empexceldata
#         for dbframe in dbframe.itertuples():
#             obj = Voter.objects.create(constituency=dbframe.constituency,caw=dbframe.caw, polling_center=dbframe.polling_center,
#                                             date_of_birth=dbframe.date_of_birth, fname=dbframe.fname, mname=dbframe.mname, sname=dbframe.sname,
#                                             sex=dbframe.sex, phone=dbframe.phone,id_passport_num=dbframe.id_passport_no )           
#             obj.save()
#         return render(request, 'voterChecker/Import_excel_db.html', {
#             'uploaded_file_url': uploaded_file_url
#         })   
#     return render(request, 'voterChecker/Import_excel_db.html',{})


# def Import_excel(request):
#     if request.method == 'POST' :
#         Voter =VoterResource()
#         dataset = Dataset()
#         new_voter = request.FILES['myfile']
#         data_import = dataset.load(new_voter.read())
#         result = VoterResource.import_data(dataset,dry_run=True)
#         if not result.has_errors():
#             VoterResource.import_data(dataset,dry_run=False)        
#     return render(request, 'voterChecker/Import_excel_db.html',{})

def  index(request):
	return render(request,'voterChecker/index.html')


def  search(request):
	if request.method == 'POST':
		id_num = request.POST['id_num']
		if id_num[:3]=='000':
			id_num = id_num[3:]
			try:
				profile = Voter.objects.get(id_passport_num=id_num)
				date = str(profile.date_of_birth)
				date=date.split(' ')[0]
				return render(request,'voterChecker/search.html',{'id_num':profile,'zeros':'000','date':date})
			except Voter.DoesNotExist:
				return render(request,'voterChecker/index.html',{'message':'ID/Passport Not Found'})
				
				# return render(request,'voterChecker/index.html')	
		elif (id_num[:2]=='00'):
			id_num = id_num[2:]
			try:
				profile = Voter.objects.get(id_passport_num=id_num)
				date = str(profile.date_of_birth)
				date=date.split(' ')[0]
				return render(request,'voterChecker/search.html',{'id_num':profile,'zeros':'00','date':date})
			except Voter.DoesNotExist:
				return render(request,'voterChecker/index.html',{'message':'ID/Passport Not Found'})
		elif(id_num[0]=='0'):
			id_num = id_num[1:]
			try:
				profile = Voter.objects.get(id_passport_num=id_num)
				date = str(profile.date_of_birth)
				date=date.split(' ')[0]
				return render(request,'voterChecker/search.html',{'id_num':profile,'zeros':'0','date':date})
			except Voter.DoesNotExist:
				return render(request,'voterChecker/index.html',{'message':'ID/Passport Not Found'})
		else:
			try:
				profile = Voter.objects.get(id_passport_num=id_num)
				date = str(profile.date_of_birth)
				date=date.split(' ')[0]
				return render(request,'voterChecker/search.html',{'id_num':profile,'date':date})
			except Voter.DoesNotExist:
				return render(request,'voterChecker/index.html',{'message':'ID/Passport Not Found'})
	else:
		return render (request,"voterChecker/index.html")