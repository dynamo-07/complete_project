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
def mensshirt(request):
    return render(request,'menshirt.html')
def menspant(request):
    return render(request,'menspant.html')
def menstshirt(request):
    return render(request,'menstshirt.html')
def womenk(request):
    return render(request,'womenk.html')
def women(request):
    return render(request,'women.html')
def kidpant(request):
    return render(request,'kidpant.html')
def kidshirt(request):
    return render(request,'kidshirt.html')
def kidtshirt(request):
    return render(request,'kidtshirt.html')