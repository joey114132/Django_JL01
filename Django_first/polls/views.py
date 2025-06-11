from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Count

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
#CRUD
#생성하기
class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ["question_text","pub_date"]
    template_name = "polls/question_form.html"
    success_url = reverse_lazy("polls:index")
    
#읽기
class QuestionUpdateView(generic.UpdateView):
    model = Question
    fields = ["question_text","pub_date"]
    template_name = "polls/question_form.html"
    success_url = reverse_lazy("polls:index")
    
#삭제하기
class QuestionDeleteView(generic.DeleteView):
    model = Question
    # fields = ["question_text","pub_date"]
    template_name = "polls/question_form_delete.html"
    success_url = reverse_lazy("polls:index")
    
def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]

def question_list(request):
    questions = Question.objects.annotate(num_choices=Count('choice'))
    return render(request, 'polls/question_list.html', {'questions': questions})