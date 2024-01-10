from django.http import HttpResponse
from django.views.generic import ListView, CreateView, View, DetailView
from core.models import UserModel, ContactModel, AboutModel, BlogModel, CommentModel, CategoryModel
from core.forms import RegisterForm, LoginForm, CommentModelForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class RegisterView(SuccessMessageMixin, CreateView):
    model = UserModel
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Registration process is successful. You can log in now'
    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'login_form': LoginForm()
        }
        return render(request, 'login.html', context = context)
    
    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password incorrect')
        return render(request, 'login.html', context = {'login_form': LoginForm()})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')

def ContactView(request):
    if request.method == "GET":
        contact = ContactModel.objects.first()
        context = {'contact': contact}
        return render(request, 'contact.html', context)

def AboutView(request):
    if request.method == "GET":
        about = AboutModel.objects.all()
        context = {'context': about}
        return render(request, 'about.html', context)

class BlogView(ListView):
    model = BlogModel
    context_object_name = 'blogs'
    template_name='blog.html'

class BlogDetailView(DetailView, CreateView):
    model = BlogModel
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'
    form_class = CommentModelForm
    
    def form_valid(self, form, *args, **kwargs):
        blog = BlogModel.objects.get(slug = self.kwargs.get('slug'))
        user = self.request.user
        form.instance.blog = blog
        form.instance.user = user
        form.instance.save()
        messages.success(self.request, 'Your comment added')
        return redirect('blog-detail', blog.slug)
    
    def form_invalid(self, form):
        ctx = {}
        ctx['blog'] = BlogModel.objects.get(slug = self.kwargs.get('slug'))
        ctx['comments'] = CommentModel.objects.filter(blog = ctx['blog'].id).all()
        ctx['form'] = form
        return self.render_to_response(ctx)
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentModelForm()
        context['comments'] = CommentModel.objects.filter(blog = self.object.id).all().order_by('-created_at')
        return context