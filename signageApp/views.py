from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
def test(request):
    return render(request,'test.html')
    
def test(request):
    return render(request,'rank.html')
"""

def adv(request):
    return render(request,'adv.html')