from django.shortcuts import render
from  django.views.generic import  ListView
from .models import  Member

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name ='app/index.html'
    context_object_name ='profiles'
    ordering =['name']

