from django.shortcuts import render,redirect
from  django.views.generic import  ListView,DeleteView,CreateView,UpdateView
from .models import  Member
from django.contrib.auth import login,authenticate
from .forms import UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name ='app/index.html'
    context_object_name ='profiles'
    ordering =['name']
    def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                return Member.objects.filter(name__icontains=query) | Member.objects.filter(phonenumber__icontains=query)
            else:
                return Member.objects.filter(user=self.request.user)

class MemberDeleteView(DeleteView):
        model = Member
        success_url = '/'
class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'
class MemberUpdateView(UpdateView):
    model = Member
    fields = '__all__'

def regist(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        uname=form.save(commit=False)
        uname.set_password(password)
        uname.save()
        uname=authenticate(username=username, password=password)
        login(request,uname)
        return redirect('app:index')
    return render(request,'app/register.html',{'form':form})


