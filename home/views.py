from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .models import *
from .forms import ContactForm, CommentForm

class view_portofolio(TemplateView):

    template_name = 'home/portofolio.html'

    def get(self, request):
        interests = Interest.objects.all()

        projects = {}
        for i in interests:
            projects[i.title] = Project.objects.filter(category=i.id)

        args = {'projects': projects, 'interests': interests}

        return render(request, self.template_name, args)

# def view_home_page(request):
#     return render(request, 'home/homepage.html')


class view_home_page(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):

        commentform = CommentForm()

        public_comment = Comment.objects.all().order_by('-posted_at')

        experiences = Experience.objects.all()

        project_blog_posts = Project_Blog_Post.objects.all().order_by('posted_at')

        personal_blog = Personal_Blog.objects.filter(privacy='public').order_by('posted_at')

        args = {'personal_blog': personal_blog, 'project_blog_posts': project_blog_posts, 'experiences': experiences,
                'Comments': public_comment, 'form': commentform}

        return render(request, self.template_name, args)

    def post_comment(request):

        form = CommentForm(request.POST)

        form.save()

        return redirect('homepage')


class view_about_page(TemplateView):
    template_name = 'home/about.html'

    def get(self, request):
        timeline = TimeLine.objects.order_by('year')
        details = Personal_Detail.objects.all().order_by('position')
        experiences = Experience.objects.all()
        args = {'timeline': timeline, 'details': details, 'experiences': experiences}

        return render(request, view_about_page.template_name, args)


class view_projects(TemplateView):
    template_name = 'home/projects.html'

    def get(self, request):
        projects = Project.objects.all().order_by('-category')

        project_blog = Project_Blog.objects.all()

        project_blog_posts = Project_Blog_Post.objects.all()
        # for p in project_blog :
        #     project_blog_posts[p.blog.title] = Project_Blog_Post.objects.filter(blog=p.id)

        args = {'projects': projects, 'project_blog': project_blog, 'project_blog_posts': project_blog_posts }

        return render(request, self.template_name, args)

class my_blog(TemplateView):
    template_name = 'home/blog.html'

    def get(self, request):

        project_blog = Project_Blog.objects.all()

        project_blog_posts = Project_Blog_Post.objects.all().order_by('-posted_at')

        personal_blog = Personal_Blog.objects.all().order_by('-posted_at')

        args = {'personal_blog': personal_blog, 'project_blog': project_blog, 'project_blog_posts': project_blog_posts }

        return render(request, self.template_name, args)



class view_contact_page(TemplateView):
    template_name = 'home/contact.html'

    def contact_us(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            form.save()

            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
                print(message)
                send_mail('New Enquiry', message, sender_email, ['admin@example.com'])
        else:
            form = ContactForm()

        return render(request, 'home/contact.html', {'form': form})
#
# class my_jumbotron(TemplateView):
#     template_name = 'home/.html'
#
#     def get(self, request):
#
#         project_blog_posts = Project_Blog_Post.objects.all().order_by('-posted_at')
#
#         personal_blog = Personal_Blog.objects.filter(privacy='public').order_by('-posted_at')
#
#         args = {'personal_blog': personal_blog, 'project_blog_posts': project_blog_posts}
#
#         return render(request, self.template_name, args)

