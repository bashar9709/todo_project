from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.contrib import messages
from app.formss import TodoForm
from datetime import datetime
from app.models import TodoModel
# Create your views here.


# showing current task
def home(request):
    data = TodoModel.objects.all()
    return render(request,'base.html',{'data': data})


# showing completed task
def Completed_Task_show(request): 
    data = TodoModel.objects.filter(status='COMPLETED')
    return render(request,'taskcompleted.html',{'data': data})

# add a new task
def Task_add(request):
    if request.method=="POST":
       form = TodoForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm() 
    return render(request,'taskadd.html',{'form':form})


#delete task  status
def task_delete(request,id): 
      current = TodoModel.objects.get(pk=id)
      current.delete()
      messages.success(request,'successful deleted!')
      return redirect('home')
  
  
#  show details task 
class Task_Details(DetailView):
    template_name = 'taskdetails.html'
    model =  TodoModel
    context_object_name = 'data'
    pk_url_kwarg = 'id'
    
   
def complete_editTask(request,id):
    task = TodoModel.objects.get(pk = id)
    form = TodoForm(instance = task)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'taskadd.html',{'form':form})    
   


#complete the task    
def CompletedTask(request, id):
    task = TodoModel.objects.get(pk = id)
    task.is_completed = True
    task.finished_date = datetime.now()
    task.save()
    return redirect('see_completed_task')
    
   
   
   

