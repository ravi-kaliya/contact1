from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from contact1djapp.models import Contact

# Create your views here.
def contact(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        add = request.POST.get('address')
        add2 = request.POST.get('address2')

        city  = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        contact = Contact(firstname=firstname,lastname=lastname,add=add,add2=add2,city=city,state=state,zip=zip,date=datetime.today())
        contact.save()
    return render(request,'contact.html')