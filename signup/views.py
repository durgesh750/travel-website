from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import siteUser, review as rw, destination, history, state as st
from django.shortcuts import render, redirect, get_object_or_404


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

global authentication
authentication=0
slist=[]

'''def home(request):     
	States = st.objects.all()
	uname = 'abc'
	return render(request,'homepage.html',{'states':States,'auth':authentication,'uname':uname}) 
'''


def home(request):     
    States = st.objects.all()
    uname = 'abc'
    #if request.method !='GET':
     #  uname = 'abc'
       # return render(request,'homepage.html',{'states':States,'auth':authentication,'uname':uname}) 
		
    #if request.method == 'GET':
     #   States = st.objects.all()
      #  uname=request.GET['user']
       # siteuser=siteUser.objects.get(username=uname)
        #return render(request,'homepage.html',{'states':States,'auth':authentication,'uname':uname})
    return render(request,'homepage.html',{'states':States,'auth':authentication,'uname':uname})
	
def homesecond(request):
    if request.method == 'GET':
        States = st.objects.all()
        uname=request.GET['user']
        siteuser=siteUser.objects.get(username=uname)
        return render(request,'homepage.html',{'states':States,'auth':authentication,'uname':uname})
	


def signup(request):
	msg=""
	uname = 'abc'
	States = st.objects.all()   
	if request.method=='POST':
		fname=request.POST['firstName']
		lname=request.POST['lastName']
		email=request.POST['email']
		uname=request.POST['userName']
		password=request.POST['password']
		passwordA=request.POST['passwordAgain']
		if password == passwordA:
			
			
			siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
			return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
		else:
			msg="Passwords didn't match"
			return render(request, 'signup.html',{'msg':msg,'auth':authentication,'uname':uname})
	return render(request, 'signup.html',{'msg':msg,'auth':authentication,'uname':uname})
	
def login(request):
	msg=""
	States = st.objects.all() 
	uname = 'abc'
	authentication=0
	if request.method=='POST':
		uname=request.POST['userName']
		password=request.POST['password']
		users=siteUser.objects.all()
		for user in users:
			if uname==user.username and password==user.password:
				#authentication=1
				return render(request,'homepage.html',{'auth':authentication,'states':States,'uname':uname})
				#return HttpResponse('success')
			if uname=="admin" and password=="password":
				#authentication=1
				return render(request,'admin.html',{'auth':authentication,'states':States,'uname':uname})
		msg="Incorrect username or password"
		return render(request,'login.html',{'msg':msg,'auth':authentication,'uname':uname})
	return render(request,'login.html',{'auth':authentication,'uname':uname})
	
def description(request):
	msg=""
	if request.method == 'GET':
		pk = request.GET['pk']
		user = request.GET['user']
	dest=destination.objects.get(place=pk)
	return render(request, 'description.html',{'dest':dest,'auth':authentication,'uname':user})
	
def state(request):
	if request.method == "GET":
		pk = request.GET['pk']
		uname = request.GET['user']
		place = st.objects.get(name=pk)
		dest = destination.objects.all()
		a = ''.join(uname)
		#for i in range(3):
		if a == 'abc' :
			errorMsg = "Login First"
			return render(request, 'error.html', {'errorMsg':errorMsg,'auth':authentication,'uname':uname})
	if request.method == "POST":
		pk = request.GET['p']
		uname = request.GET['user']
		wish=request.GET['wish']
		user= siteUser.objects.get(username=uname)
		place = destination.objects.get(place=wish)
		dest = destination.objects.all()
		newhistory = history.objects.create(uid=user,recent='abc', wishlist=wish)
		errorMsg="success"
		return render(request, 'error.html', {'errorMsg':errorMsg,'auth':authentication,'uname':uname})
		
	return render(request, 'destinations.html',{'state':place,'auth':authentication,'dest':dest,'uname':uname,'a':a,'pk':pk})
	
def review(request):
	l=[]
	if request.method == "GET":
		user = request.GET['user']
		pk = request.GET['pk']
		user = "".join(user)
		pk = "".join(pk)
		userReviews = rw.objects.all()
		for ureview in userReviews:
			if ureview.did.place == pk:
				l.append(ureview.review)
		return render(request,'review.html',{'list':l,'auth':authentication,'uname':user,'dest':pk})
		
	return render(request,'review.html',{'auth':authentication,'uname':user,'dest':pk})
	
def writereview(request):
	if request.method == "GET":
		user = request.GET['user']
		pk = request.GET['pk']
	if request.method == 'POST':
		pk = request.GET['p']
		uname = request.GET['user']
		nreview = request.POST['message']
		user = siteUser.objects.get(username=uname)
		stateName = destination.objects.get(place=pk)
		newreview = rw.objects.create(uid=user, did=stateName, review= nreview)
		errorMsg="Successful"
		return render(request, 'error.html',{'errorMsg':errorMsg,'auth':authentication})
	return render(request, 'writereview.html',{'pk':pk,'uname':user,'auth':authentication})
	
'''def search(request):
	#state = st.objects.all()
	if request.method == 'POST':
		query = request.POST['search']
		stateName = st.objects.all()
		for sname in stateName:
			if sname.name == query:
				return render(request, 'search.html', {'auth':authentication,'query':query, 'state':stateName})
	errorMsg="0 results found"
	return render(request, 'error.html', {'auth':authentication,'errorMsg':errorMsg})'''
	
	
def search(request):
	if request.method == 'GET':
		uname=request.GET['user']
	#state = st.objects.all()
	if request.method == 'POST':
		query = request.POST['search']
		stateName = st.objects.all()
		uname=request.GET['user']
		for sname in stateName:
			if sname.name == query:
				slist.append(query)
				return render(request, 'search.html', {'auth':authentication,'query':query, 'state':stateName,'slist':slist,'uname':uname})
	errorMsg="0 results found"
	return render(request, 'error.html', {'auth':authentication,'errorMsg':errorMsg})
	
def account(request):
	if request.method == 'GET':
		histories = history.objects.all()
        
		uname=request.GET['user']
        #firstName=request.GET['fname']
        #emailid=request.GET['email']
        #password1=request.GET['password']
		user = siteUser.objects.get(username=uname)
		return render(request,'account.html',{'uname':uname,'auth':authentication,'user':user,'histories':histories})

def admin(request):
	return render(request, 'admin.html')
	
def databases(request):
	if request.method == 'GET':
		id = request.GET['id']
		id = "".join(id)
		id = int(id)
		user = siteUser.objects.all()
		reviews = rw.objects.all()
		histories = history.objects.all()
		destinations = destination.objects.all()
		states = st.objects.all()
		return render(request, 'databases.html', {'user':user,'reviews':reviews,'histories':histories,'destinations':destinations,'states':states,'id':id})
	return render(request, 'databases.html')
	
def userchange(request):
	if request.method == 'GET':
		var = request.GET['value']
		users = siteUser.objects.get(username=var)
	if request.method=='POST':
		val=request.GET['value']
		use=siteUser.objects.get(username=val)
		use.firstName=request.POST['firstName']
		use.lastname=request.POST['lastName']
		use.email=request.POST['email']
		use.username=request.POST['userName']
		use.password=request.POST['password']
		use.active=request.POST['active']
		use.save()
		#siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
		#return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
		return HttpResponse('success')
	return render(request, 'userchange.html', {'users':users,'var':var})
	
def statechange(request):
	if request.method == 'GET':
		var = request.GET['value']
		users = st.objects.get(name=var)
	if request.method=='POST':
		val=request.GET['value']
		use=st.objects.get(name=val)
		use.name=request.POST['firstName']
		use.save()
		#siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
		#return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
		return HttpResponse('success')
	return render(request, 'statechange.html', {'users':users,'var':var})
	
def historychange(request):
	if request.method == 'GET':
		var = request.GET['value']
		use = siteUser.objects.get(username=var)
		users = history.objects.get(uid=use)
	if request.method=='POST':
		val=request.GET['value']
		val="".join(val)
		users = siteUser.objects.get(username=val)
		use=history.objects.get(uid=users)
		use.uid=use.uid
		use.recent=request.POST['firstName']
		use.wishlist=request.POST['lastname']
		use.save()
		#siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
		#return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
		return HttpResponse('success')
	return render(request, 'historychange.html', {'users':users,'var':var})
	
def reviewchange(request):
	if request.method == 'GET':
		var = request.GET['value']
		#use = siteUser.objects.get(username=var)
		users = rw.objects.get(id=var)
	if request.method=='POST':
		val=request.GET['value']
		#val="".join(val)
		#users = siteUser.objects.get(id=val)
		use=rw.objects.get(id=val)
		use.id=use.id
		use.uid=use.uid
		use.did=use.did
		use.review=request.POST['firstName']
		use.save()
		#siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
		#return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
		return HttpResponse('success')
	return render(request, 'reviewchange.html', {'users':users,'var':var})
	
def destinationchange(request):
	if request.method == 'GET':
		var = request.GET['value']
		#use = siteUser.objects.get(username=var)
		users = destination.objects.get(place=var)
	if request.method=='POST':
		val=request.GET['value']
		val="".join(val)
		#users = destination.objects.get(place=val)
		use=destination.objects.get(place=val)
		use.place=request.POST['firstName']
		use.state=request.POST['lastName']
		use.desc=request.POST['email']
		use.imghome=request.POST['userName']
		use.img1=request.POST['password']
		use.img2=request.POST['active']
		use.img3=use.img3
		use.save()
		#siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
		#return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
		return HttpResponse('success')
	return render(request, 'destinationchange.html', {'users':users,'var':var})
	
def passwordchange(request):
	errorMsg=""
	if request.method == 'GET':
		var = request.GET['value']
		users = siteUser.objects.get(username=var)
		#users = destination.objects.get(place=var)
	if request.method=='POST':
		val=request.GET['value']
		usern=request.POST['username']
		passw=request.POST['oldpassword']
		npassw=request.POST['newpassword']
		val="".join(val)
		use=siteUser.objects.get(username=val)
		if usern == use.username and passw == use.password:
		
		#users = destination.objects.get(place=val)
		
			use.firstName=use.firstName
			use.lastname=use.lastname
			use.email=use.email
			use.username=use.username
			use.password=npassw
			use.active=use.active
			use.save()
			errorMsg="Success"
		#siteuser=siteUser.objects.create(username=uname,firstName=fname,lastname=lname,email=email,password=password)
		#return render(request, 'homepage.html',{'states':States,'auth':authentication,'uname':uname})
			return render(request, 'error.html', {'errorMsg':errorMsg,'auth':authentication,'uname':uname})
		else:
			errorMsg = "Incorrect username or password "
			return render(request, 'passwordchange.html', {'users':use,'var':val,'errorMsg':errorMsg})
	return render(request, 'passwordchange.html', {'users':users,'var':var})
	
def recent_search(request):
	
	if request.method == 'GET':
        
		uname=request.GET['user']
        #firstName=request.GET['fname']
        #emailid=request.GET['email']
        #password1=request.GET['password']
		siteuser = siteUser.objects.get(username=uname)
		return render(request, 'recentsearch.html', {'auth':authentication,'slist':slist,'uname':uname})
	#return render(request,'account.html',{'uname':uname,'auth':authentication,'user':siteuser.username})
	
def delete(request):
	if request.method=="GET":
		id = request.GET['identity']
		name = request.GET['user']
		id = int("".join(id))
		name="".join(name)
		if id==1:
			users=siteUser.objects.get(username=name)
			users.delete()
		if id==2:
			users=state.objects.get(name=name)
			users.delete()
		if id==3:
			users=history.objects.get(id=name)
			users.delete()
		if id==4:
			users=rw.objects.get(id=name)
			users.delete()
		if id==5:
			users=destination.objects.get(place=name)
			users.delete()
		return HttpResponse('success')