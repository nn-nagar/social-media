from django.db.models import Q
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
from django.views.generic import ListView, DetailView, UpdateView

from college.models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from college.models import Profile


def home(req):
    return render(req, "index.html")


@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        if self.request.user.is_superuser:
            return Notice.objects.order_by('-id')
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by('-id')


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice

@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch"]
