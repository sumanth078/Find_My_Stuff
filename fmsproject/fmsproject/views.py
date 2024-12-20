from django.shortcuts import render

def indexpage(request):
    return render(request,"index.html")

def aboutuspage(request):
    return render(request,"aboutus.html")

def contactuspage(request):
    return render(request,"contactus.html")

# def registrationPage(request):
#     return render(request, "registration.html")

def testpage(request):
    return render(request, "test.html")
