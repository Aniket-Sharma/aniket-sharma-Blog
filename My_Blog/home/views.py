from django.shortcuts import render
from django.views.generic import TemplateView

#
# def view_portofolio(request):
#     return render(request, 'home/portofolio.html')

# def view_home_page(request):
#     return render(request, 'home/homepage.html')


class view_home_page(TemplateView):
    template_name = 'home/homepage.html'
