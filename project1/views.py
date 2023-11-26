from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'user': 'Александр'})
    if request.method == 'POST':
        loginn = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        return redirect('/profile/')
        #return HttpResponse(f'<h1>авторизация прошла успешно</h1>Login: {loginn}  Email: {email}  Password: {password}')
    return render('такой запрос не предусмотрен')