from django.shortcuts import render,redirect,reverse
from . models import Enquiry,Login,Student
from datetime import date
from django.contrib import messages
from adminapp.models import Program,Branch,Year
from adminapp.models import News

# Create your views here.
def index(request):
    ns=News.objects.all()
    return render(request,"index.html",locals())
def aboutus(request):
    ns=News.objects.all()
    return render(request,"aboutus.html",locals())
def registration(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        regdate=date.today()
        usertype='student'
        status='false'
        stu=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,address=address,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate)
        log=Login(userid=rollno,password=password,usertype=usertype,status=status)
        stu.save()
        log.save()
        messages.success(request,'Student Registration is done')
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    ns=News.objects.all()
    return render(request,"registration.html",locals())
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj.usertype=="student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=='admin':
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
            elif obj.usertype=="admin":
                messages.success(request,"Welcome Admin")
        except:
            messages.success(request,'Invalid User')
    ns=News.objects.all()
    return render(request,"login.html",locals())
def contactus(request):
    if request.method=="POST":
     name=request.POST['name']
     gender=request.POST['gender']
     address=request.POST['address']
     contactno=request.POST['contactno']
     emailaddress=request.POST['emailaddress']
     enquirytext=request.POST['enquirytext']
     enquirydate=date.today()
     enq=Enquiry(name=name, gender=gender, address=address, contactno=contactno, emailaddress=emailaddress,enquirytext=enquirytext, enquirydate=enquirydate)
     enq.save()
     messages.success(request,'Enquiry is submitted')
    ns=News.objects.all()
    return render(request,"contactus.html",locals())