from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cpu, Gpu, Question, Choice

# Create your views here.
class HomeView(TemplateView):
    template_name = "quiz/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['cpu'] = Cpu.objects.all()[:8].values()
        context['gpu'] = Gpu.objects.all()[:8].values()
        return context

class PcBuilderView(TemplateView):
    template_name = "quiz/quiz.html"
    questions = Question.objects.all()
    def get_context_data(self, **kwargs):
        context = super(PcBuilderView, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context
