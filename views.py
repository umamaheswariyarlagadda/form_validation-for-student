from django.shortcuts import render,HttpResponse
from .forms import PostForm


# Create your views here.
def home(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data submitted successfully.")
        return render(request,'home.html',{'form':form})
    form = PostForm()
    return render(request,'home.html',{'form':form})
