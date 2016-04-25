from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import sys
sys.path.append("/home/ubuntu/workspace/github")
import Driver

# Create your views here.

class ConvexHullView(generic.ListView):
    template_name = 'algorithms/convexhull.html'
    #context_object_name = 'filepath'
    
    def post(self, request, *args, **kwargs):
        text = request.POST.get('input_text', '')
        min_x = int(request.POST.get('min_x', ''))
        max_x = int(request.POST.get('max_x', ''))
        min_y = int(request.POST.get('min_y', ''))
        max_y = int(request.POST.get('max_y', ''))
        number_of_points = int(request.POST.get('number_of_points', ''))
        filepath = Driver.run(input_text = text, number_of_points = number_of_points,
            rangeX = (min_x,max_x), rangeY = (min_y,max_y))
        context = {'filepath':filepath}
        return render(request, 'algorithms/convexhull.html', context)
    
    def get_queryset(self):
        return None

# def compute(request):
#     text = request.POST.get('input_text', '')
#     filepath = Driver.run2(text)
#     return HttpResponseRedirect(reverse('algorithms:simple', args=(text,)))
    
# def simple(request):
#     text = request.POST.get('input_text', '')
#     filepath = Driver.run2(text)
#     context = {'filepath': filepath}
    
#     return render(request, 'algorithms/simple.html', context)

class ResultsView(generic.ListView):
    template_name = 'algorithms/results.html'
    context_object_name = 'text'

    def get_queryset(self):
        return self.args[0]