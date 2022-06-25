from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'name':'bablu'}
    d={'a':100,'b':200,'c':50}
    return render(request,'hai.html',context=d)


def looping(request):
    d={'name':'nani'}
    return render(request,'looping.html',context=d)
