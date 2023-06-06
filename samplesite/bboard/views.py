from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.template import loader
from .models import Bb, Rubric
from .forms import BbForm


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/bb_create.html'  # путь к файлу шаблона, создающего страницу с формой
    form_class = BbForm  # ссылка на класс формы, связанной с моделью
    success_url = reverse_lazy('index')  # интернет адрес для перенаправления после успешного сохранения данных

    def get_context_data(self, **kwargs):  # переопределили метод, чтобы еще выводились рублики
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
