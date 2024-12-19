# from django.shortcuts import render
# from .forms import UserRegistrationForm
# from .models import UserRegistration
# from django.db.models import Q
# from django.http import HttpResponse

# # Create your views here.

# def registrationPage(request):
#     form = UserRegistrationForm()
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = "Successfully Registered 🥳"
#             return render(request,"registration.html",{"msg":msg})
#         else:
#             msg="Registration Failed 😥"
#             return render(request,"registration.html",{"msg":msg})
#     return render(request,"registration.html",{"form":form})

#     # return render(request,"registration.html")

# def loginPage(request):
#     return render(request,"login.html")

# def checkuserlogin(request):
#     sid = request.POST["studentid"]
#     pwd = request.POST["password"]
#     flag = UserRegistration.objects.filter(Q(studentid=sid) & Q(password=pwd))
#     print(flag)
#     if flag:
#         user = UserRegistration.objects.get(studentid=sid)
#         print(user)
#         print(user.id, user.fullname)
#         return render(request,"indexhome.html")
#     else:
#         msg="Login Failed"
#         return render(request, "login.html", {"msg":msg})
    
# def userlogout(request):
#     return render(request,"seekerlogin.html")
    
# def indexhome(request):
#     return render(request,"indexhome.html")

# def postBookPage(request):
#     return render(request,"postBook.html")

# def postLostPage(request):
#     return render(request,"postLost.html")


# from django.shortcuts import render
# from .forms import UserRegistrationForm
# from .models import UserRegistration
# from django.db.models import Q
# from django.http import HttpResponse

# # Create your views here.

# def registrationPage(request):
#     form = UserRegistrationForm()
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = "Successfully Registered 🥳"
#             return render(request,"registration.html",{"msg":msg})
#         else:
#             # Changed: Returning form with errors to show validation issues
#             return render(request,"registration.html",{"form":form})
#     return render(request,"registration.html",{"form":form})

# def loginPage(request):
#     return render(request,"login.html")

# def checkuserlogin(request):
#     sid = request.POST["studentid"]
#     pwd = request.POST["password"]
#     flag = UserRegistration.objects.filter(Q(studentid=sid) & Q(password=pwd))
#     print(flag)
#     if flag:
#         user = UserRegistration.objects.get(studentid=sid)
#         print(user)
#         print(user.id, user.fullname)
#         return render(request,"indexhome.html")
#     else:
#         msg="Login Failed"
#         return render(request, "login.html", {"msg":msg})

# def userlogout(request):
#     return render(request,"seekerlogin.html")

# def indexhome(request):
#     return render(request,"indexhome.html")

# def postBookPage(request):
#     return render(request,"postBook.html")

# def postLostPage(request):
#     return render(request,"postLost.html")


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import UserRegistrationForm
# from .models import UserRegistration

# def registrationPage(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Successfully Registered 🥳")
#             return redirect('login')  # Adjust to wherever you'd like users to go post-registration
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = UserRegistrationForm()  # Create a new form for a GET request
#     return render(request, "registration.html", {"form": form})

# def loginPage(request):
#     return render(request, "login.html")

# def checkuserlogin(request):
#     sid = request.POST.get("studentid")
#     pwd = request.POST.get("password")
#     user = UserRegistration.objects.filter(studentid=sid, password=pwd).first()
#     if user:
#         return render(request, "indexhome.html", {"user": user})
#     else:
#         messages.error(request, "Login Failed. Incorrect Student ID or Password.")
#         return render(request, "login.html")

# def userlogout(request):
#     # Assuming you're clearing some session data or similar
#     request.session.flush()
#     return render(request, "login.html")  # Redirect to login page after logout

# def indexhome(request):
#     # Load home page after login
#     return render(request, "indexhome.html")

# def postBookPage(request):
#     # Load a page for posting a book, ensure you have a form and a view to handle this if necessary
#     return render(request, "postBook.html")

# def postLostPage(request):
#     # Load a page for posting lost items, ensure you have a form and a view to handle this if necessary
#     return render(request, "postLost.html")


# -------------------------------

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistration

def registrationPage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered 🥳")
            return redirect('registration')  # Redirect to the same registration page to show the popup
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()  # Create a new form for a GET request
    return render(request, "registration.html", {"form": form})

def loginPage(request):
    return render(request, "login.html")

def checkuserlogin(request):
    sid = request.POST.get("studentid")
    pwd = request.POST.get("password")
    user = UserRegistration.objects.filter(studentid=sid, password=pwd).first()
    if user:
        return render(request, "indexhome.html", {"user": user})
    else:
        messages.error(request, "Login Failed. Incorrect Student ID or Password.")
        return render(request, "login.html")

def userlogout(request):
    request.session.flush()
    return render(request, "login.html")  # Redirect to login page after logout

def indexhome(request):
    return render(request, "indexhome.html")

def postBookPage(request):
    return render(request, "postBook.html")

def postLostPage(request):
    return render(request, "postLost.html")
