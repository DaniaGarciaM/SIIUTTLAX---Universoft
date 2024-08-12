from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    try:
        if user.professor:
            type_user = 'professor'
           # return redirect('home:professor')
    except:
        type_user ='other'
        
    if type_user == 'other':
        try:
            if user.student:
                type_user = 'student'
                #return redirect('home:student')
                
        except:
            type_user = 'other'
        
    context = {
        "user": user,
        "type_user": type_user
    }
    print(type_user)
    if type_user == 'professor':
        return redirect('home:professor')
    elif type_user == 'student':
        return redirect('home:student')
    else:
        return render(request, 'home/home.html', context)
        
    # return render(request, 'home/home.html', {'user':user})
    
def student(request):
    user = request.user
    student = user.student
    group = student.group_set.all().first()
    career = group.career
    
    context = {
        'student': student,
        'group': group,
        'career': career
    }
    
    return render(request, 'home/student.html', context)
# hola mundo
def professor(request):
    user = request.user
    professor = user.professor
    group = professor.group_set.all().first()
    career = group.career
    
    context = {
        'professor': professor,
        'group': group,
        'career': career
    }
    
    return render(request, 'home/professor.html', context)