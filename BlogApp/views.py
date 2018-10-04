from django.shortcuts import render,redirect,get_object_or_404
from .models import Qoute
from django.views import generic
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .forms import Qouteform



# Create your views here.
def index(request):
    return render(request,'blogApp/index.html')






def input(request):
    qoutes=Qoute.objects.all()
    context={'qoutes':qoutes}
    return render(request,'blogApp/input.html',context)
  
def save(request):
    if request.method=='POST':#if the form has been submitted
        form=Qouteform(request.POST,request.FILES)# the form bounded to data
        if form.is_valid():
            qoute=form.save()
            qout.save()
    else: 
     form=Qouteform()       
    #qoute=Qoute(title=request.POST['title'],author=request.POST['author'],text=request.POST['text'])#,picture=request.POST['picture']
    #qoute.save()
    return redirect('/input')

def display(request):
    qoutes=Qoute.objects.all()
    context={'qoutes':qoutes}
    return render(request,'blogApp/display.html',context)
    
def delete(request,id):
    qoute=Qoute.objects.get(id=id)
    qoute.delete()
    return redirect('/display')





def update(request,id):
    qoute=Qoute.objects.get(id=id)
    qoute.author=request.POST['author']
    qoute.text=request.POST['text']
    qoute.title=request.POST['title']
    qoute.save()
    return redirect('/display')
    

    
class writer(generic.DetailView) :
    model=Qoute
    template_name='blogApp/writer.html'



class edite(generic.DetailView) :
    model=Qoute
    template_name='blogApp/edite.html'  





    

            




        


        




     
    
  




      