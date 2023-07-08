from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from .models import SongModel, PointModel
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import PointModelForm

# Create your views here.

def listfunc(request):
    object_list = SongModel.objects.all()
    return render(request, "list.html", {"object_list":object_list})

def detailfunc(request, pk):
    songmodel = get_object_or_404(SongModel, pk=pk)
    return render(request, "detail.html", {"songmodel":songmodel})

class SongCreate(CreateView):
    template_name = "songcreate.html"
    model = SongModel
    fields = ("title",)
    success_url = reverse_lazy("list")

def PointCreate(request):
    if request.method == "POST":
        form = PointModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = PointModelForm()
    return render(request, "create2.html", {"form":form})

class SongDelete(DeleteView):
    template_name = "delete.html"
    model = SongModel
    success_url = reverse_lazy("list")




