from django.contrib import admin
from app.models import TodoModel

# Register your models here.
@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','is_completed','first_date','last_date','category','status','finished_date')


