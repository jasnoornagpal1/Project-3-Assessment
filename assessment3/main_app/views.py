from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.edit import CreateView, UpdateView
from .forms import WidgetForm

# Create your views here.

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"

class WidgetUpdate(UpdateView):
    model = Widget
    fields = "__all__"

def home(request):
    return render(request,"index.html")

def widget_index(request):
    widget = Widget.objects.all()
    return render(request, 'templates/index.html', { 'widget': widget })

def widget_detail(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget_form = FeedingForm()
    return render(request, 'templates/index.html', {
        'widget' : widget, 'widget_form' : widget_form,
    })

def widget_add(request, widget_id):
	# create the ModelForm using the data in request.POST
    form = WidgetForm(request.POST)
  # validate the form
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.widget_id = widget_id
        new_widget.save()
    return redirect('detail', widget_id=widget_id)
