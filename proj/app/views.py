from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def mens(request):
    return render(request,'mens.html')
def womens(request):
    return render(request,'womens.html')
def childrens(request):
    return render(request,'childerns.html')
def loginpage(request):
    return render(request,'loginpage.html')
def main123(request):
    return render(request,'main123.html')