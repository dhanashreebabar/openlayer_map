from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from io import BytesIO
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        return redirect('login') 

    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('map')

        
        error_message = "Invalid username or password."
        return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  


@login_required
def map_view(request):
    username = request.user.username
    return render(request, 'registration/map.html', {'username': username})



class MapPDFView(View):
    def get(self, request):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 100, "Map PDF Content")  
        p.showPage()
        p.save()
        buffer.seek(0)
        response = FileResponse(buffer, as_attachment=True, filename='map.pdf')
        return response
