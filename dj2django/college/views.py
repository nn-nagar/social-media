from django.db.models import Q
from django.http import HttpResponseRedirect
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
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView

from college.models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from college.models import Profile

from college.models import Question


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
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(
                Q(subject__icontains=si) | Q(msg__icontains=si)).order_by('-id')


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn", "myimg", "myresume", "skills"]


class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "msg"]

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class MyList(TemplateView):
    template_name = 'college/mylist.html'

    def get_context_data(self, **kwargs):
        context = super(MyList,self).get_context_data(**kwargs)
        context["notices"] = Notice.objects.order_by("-id")[:3]
        context["questions"] = Question.objects.order_by("-id")[:3]
        return context


