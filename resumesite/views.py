from django.shortcuts import render
from .forms import ContactForm
from .models import std, resume
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from pyresparser import ResumeParser
import os
import glob
from docx import Document

def home(request):
    return render(request, 'home.html', {})


def info(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            skills_1 = form.cleaned_data['skills_1']
            skills_2 = form.cleaned_data['skills_2']
            skills_3 = form.cleaned_data['skills_3']
            skills_4 = form.cleaned_data['skills_4']
            skills_5 = form.cleaned_data['skills_5']
            skills_6 = form.cleaned_data['skills_6']

            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            description = form.cleaned_data['desc']

            experience_1_title = form.cleaned_data['experience_1_title']
            experience_1_dur = form.cleaned_data['experience_1_dur']
            experience_1_desc = form.cleaned_data['experience_1_desc']

            experience_2_title = form.cleaned_data['experience_2_title']
            experience_2_dur = form.cleaned_data['experience_2_dur']
            experience_2_desc = form.cleaned_data['experience_2_desc']

            education_10th_year = form.cleaned_data['education_10th_year']
            education_10th_uni = form.cleaned_data['education_10th_uni']
            education_10th_score = form.cleaned_data['education_10th_score']

            education_12th_year = form.cleaned_data['education_12th_year']
            education_12th_uni = form.cleaned_data['education_12th_uni']
            education_12th_score = form.cleaned_data['education_12th_score']

            education_btech_year = form.cleaned_data['education_btech_year']
            education_btech_uni = form.cleaned_data['education_btech_uni']
            education_btech_score = form.cleaned_data['education_btech_score']

            education_mtech_year = form.cleaned_data['education_mtech_year']
            education_mtech_uni = form.cleaned_data['education_mtech_uni']
            education_mtech_score = form.cleaned_data['education_mtech_score']

            use = std(name=name, email=email, phone=mobile, address=address, description=description, skill_1=skills_1, skill_2=skills_2, skill_3=skills_3,
                      skill_4=skills_4, skill_5=skills_5, skill_6=skills_6, exp_1_title=experience_1_title, exp_1_description=experience_1_desc,
                      exp_1_duration=experience_1_dur, exp_2_title=experience_2_title, exp_2_description=experience_2_desc, exp_2_duration=experience_2_dur,
                      education_10th_year=education_10th_year,
                      education_10th_uni=education_10th_uni, education_10th_score=education_10th_score, education_12th_year=education_12th_year,
                      education_12th_uni=education_12th_uni, education_12th_score=education_12th_score, education_btech_year=education_btech_year,
                      education_btech_uni=education_btech_uni, education_btech_score=education_btech_score, education_mtech_year=education_mtech_year,
                      education_mtech_uni=education_mtech_uni, education_mtech_score=education_mtech_score)
            use.save()

            data = {'name': name}
            # data['id']=str(int(std.objects.latest('id')))
            data['email'] = email
            data['skill_1'] = skills_1
            data['skill_2'] = skills_2
            data['skill_3'] = skills_3
            data['skill_4'] = skills_4
            data['skill_5'] = skills_5
            data['skill_6'] = skills_6

            data['phone'] = mobile
            data['address'] = address
            data['description'] = description

            data['exp_1_title'] = experience_1_title
            data['exp_1_dur'] = experience_1_dur
            data['exp_1_desc'] = experience_1_desc

            data['exp_2_title'] = experience_2_title
            data['exp_2_dur'] = experience_2_dur
            data['exp_2_desc'] = experience_2_desc

            data['education_10th_year'] = education_10th_year
            data['education_10th_uni'] = education_10th_uni
            data['education_10th_score'] = education_10th_score

            data['education_12th_year'] = education_12th_year
            data['education_12th_uni'] = education_12th_uni
            data['education_12th_score'] = education_12th_score

            data['education_btech_year'] = education_btech_year
            data['education_btech_uni'] = education_btech_uni
            data['education_btech_score'] = education_btech_score

            data['education_mtech_year'] = education_mtech_year
            data['education_mtech_uni'] = education_mtech_uni
            data['education_mtech_score'] = education_mtech_score
            return render(request, 'home.html', {'data': data})
            # to add more go to : forms.py
            # print(name,email)
    return render(request, 'info.html', {'form': form})


def pdf_resume(request):
    data = std.objects.last()

    template_path = 'pdf_home.html'
    context = {'data': data}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    template = get_template(template_path)
    html = template.render(context)

# create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
# if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


def analyzer(request):
    check=0
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = resume.objects.create(file=file2)
        document.save()
        check = 1

        return render(request, 'analyzer.html', {'check':check})
    return render(request, 'analyzer.html', {'check':check}) 


def analysis(request):
    list = glob.glob('D:/College/Year4/EDI/Django-Resume-Builder-master/resume_builder_django/media/*')
    filed = max(list, key=os.path.getctime)
    print(filed)
    try:
        doc = Document()
        with open(filed, 'r') as file:
            doc.add_paragraph(file.read())
        doc.save("text.docx")
        data = ResumeParser('text.docx').get_extracted_data()
    except:
        data = ResumeParser(filed).get_extracted_data()

    score = 100
    # remarks= {'page': '', 'det':'', 'exp':'', 'college':'', 'skills':''}
    remarks = {}
    if data['no_of_pages']>2:
        score = score-20
        remarks['page'] = 'Reduce number of pages'
    if not(data['name'] and data['email'] and data['mobile_number']):
        score = score-20
        remarks['det'] = 'Enter the basic and necessary details'
    if not(data['experience']):
        score = score-10
        remarks['exp'] = 'Add prior experiences if any'
    if not(data['designation']):
        score = score-10
    if not(data['company_names']):
        score = score-10
    if not(data['college_name']):
        score = score-10
        remarks['college'] = 'Enter college/school name'
    if not(data['degree']):
        score = score-10
    if len(data['skills']) < 6:
        score = score-10
        remarks['skills'] = 'Add more skills to the resume'
    if score<=80:
        remarks['des'] = 'Try a different format'

    if score>80:
        grade = 'A'
    elif score>60:
        grade = 'B'
    elif score>40:
        grade = 'C'
    elif score>20:
        grade = 'D'
    else:
        grade = 'F'
    
    return render(request, 'result.html',{'data':data, 'grade':grade, 'remarks':remarks})