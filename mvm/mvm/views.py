import datetime


from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import sendmail, matric

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def admission(request):
    return render(request, 'admission.html')

def contactus(request):
    return render(request, 'contactus.html')

def fees(request):
    return render(request, 'fees.html')

def gallery(request):
    return render(request, 'gallery.html')

def inclusive(request):
    return render(request, 'inclusive.html')

def matric(request):
    return render(request, 'matric.html')

def osla(request):
    return render(request, 'osla.html')

def special(request):
    return render(request, 'special.html')

def sports(request):
    return render(request, 'sports.html')

def contact(request):
    if request.method == "POST":
        insertvalues = sendmail()
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        mail_id = request.POST.get('email')
        message = request.POST.get('comment')
        subject = str(subject)
        body = " Name : {name}\n Email : {email}\n Message : {message}\n" .format(name=str(name), email=str(mail_id), message=str(message))

        send_mail(
            subject,
            body,
            mail_id,
            ['imrannazeer239@gmail.com']
        )
        messages.info(request, "Response registered successfully!!!, Our team will get back to you soon")
        return redirect('contact-us')


def enquirymatric(request):
    if request.method == "POST":

        applicant_name = request.POST.get('applicant_name')
        day = request.POST.get('date_day')
        month = request.POST.get('date_month')
        year = request.POST.get('date_year')
        dob = str(day)+"-"+str(month)+"-"+str(year)
        mobile_matric = request.POST.get('mobilematric')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        std = request.POST.get('std')
        nationality = request.POST.get('nationality')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        annual_income = request.POST.get('annual_income')
        community = request.POST.get('community')
        last_school = request.POST.get('last_school')
        email = request.POST.get('email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')


        subject = "Enquiry for MVM Matriculation"
        message = " Applicant Name : {name}\n Date of Birth : {dob}\n Mobile Number : {mobile}\n Gender : {gender}\n Religion : {religion}\n Standard : {std}\n Nationality : {nationality}\n Father Name : {fathername}\n Father Occupation : {fatheroccupation}\n Mother Name : {mothername}\n Mother Occupation : {motheroccupation}\n Annual Income : {annual}\n Community : {community}\n Previously Studied School : {lastschool}\n Email : {email}\n Present Address : {present}\n Permanent Address : {permanent}\n".format(name=str(applicant_name), dob=str(dob) , mobile=str(mobile_matric), gender=str(gender), religion=str(religion), std=str(std), nationality=str(nationality), fathername=str(father_name), fatheroccupation=str(father_occupation), mothername=str(mother_name), motheroccupation=str(mother_occupation), annual=str(annual_income), community=str(community), lastschool=str(last_school), email=str(email), present=str(present_address), permanent=str(permanent_address))

        send_mail(
            subject,
            message,
            email,
            ['imrannazeer239@gmail.com']
        )
        messages.info(request, "Response registered successfully!!!, Our team will get back to you soon.")
        return redirect('matric-us')

def enquiryinclusive(request):
    if request.method == "POST":

        applicant_name = request.POST.get('applicant_name')
        day = request.POST.get('date_day')
        month = request.POST.get('date_month')
        year = request.POST.get('date_year')
        dob = str(day)+"-"+str(month)+"-"+str(year)
        mobile_matric = request.POST.get('mobilematric')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        std = request.POST.get('std')
        nationality = request.POST.get('nationality')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        annual_income = request.POST.get('annual_income')
        community = request.POST.get('community')
        last_school = request.POST.get('last_school')
        email = request.POST.get('email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')


        subject = "Enquiry for MVM Inclusive School for Special Children"
        message = " Applicant Name : {name}\n Date of Birth : {dob}\n Mobile Number : {mobile}\n Gender : {gender}\n Religion : {religion}\n Standard : {std}\n Nationality : {nationality}\n Father Name : {fathername}\n Father Occupation : {fatheroccupation}\n Mother Name : {mothername}\n Mother Occupation : {motheroccupation}\n Annual Income : {annual}\n Community : {community}\n Previously Studied School : {lastschool}\n Email : {email}\n Present Address : {present}\n Permanent Address : {permanent}\n".format(name=str(applicant_name), dob=str(dob) , mobile=str(mobile_matric), gender=str(gender), religion=str(religion), std=str(std), nationality=str(nationality), fathername=str(father_name), fatheroccupation=str(father_occupation), mothername=str(mother_name), motheroccupation=str(mother_occupation), annual=str(annual_income), community=str(community), lastschool=str(last_school), email=str(email), present=str(present_address), permanent=str(permanent_address))

        send_mail(
            subject,
            message,
            email,
            ['uvaishahamed106@gmail.com']
        )
        messages.info(request, "Response registered successfully!!!, Our team will get back to you soon.")
        return redirect('inclusive-us')
