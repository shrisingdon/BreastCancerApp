from django.http import HttpResponse
from django.shortcuts import render
import joblib

def hi(request):
    return render(request,'DEMOAPP/home.html')

def demo(request):
    return render(request, "DEMOAPP/demo.html")

def result(request):
    classifier = joblib.load('model.sav')
    lis = []
    lis.append(request.GET['area'])
    lis.append(request.GET['perimeter'])
    lis.append(request.GET['radius'])
    lis.append(request.GET['concavity'])
    print(lis)
    ans = classifier.predict([lis])
    if ans == 'M':
        ans = 'Malignant'
    else:
        ans = 'Benign'
    return render(request, "DEMOAPP/result.html", {'ans': ans})

def malignant(request):
    return render(request, "DEMOAPP/malignant.html")

def benign(request):
    return render(request, "DEMOAPP/benign.html")
