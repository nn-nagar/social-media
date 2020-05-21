from django.shortcuts import render

# Create your views here
# def home(request):
#     return render(request, "index.html", {'name': 'Narendra'})
#
#
# def about(request):
#     return render(request, "about.html", {'name': 'about us'})
#
#
# def contact(request):
#     return render(request, "contact.html", {'contact': '9993780478'})
from django.views.generic import ListView, DetailView

from college.models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def home(req):
    return render(req, "index.html")


@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Notice.objects.order_by('-id')
        else:
            return Notice.objects.filter(branch=self.request.user.profile.branch).order_by('-id')


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice
