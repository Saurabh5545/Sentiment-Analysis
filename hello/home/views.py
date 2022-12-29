from django.shortcuts import render,HttpResponse
from subprocess import run,PIPE
import sys
# Create your views here.

def index(request):

    return render(request,'home.html')


def output(request):
    inpt = request.GET.get('hash')
    #out = run([sys.executable,'C://Users//ASUS//Desktop//project//test.py',inpt],shell=False,stdout=PIPE)
    run([sys.executable,'C://Users//ASUS//Desktop//django//tutorial-yt//main.py',inpt],shell=False,stdout=PIPE)
    #print(out)

    return render(request,'result.html')