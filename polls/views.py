from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Count
from collections import Counter

from .models import Category, Question, Choice, PersonalityResult


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "categories"

    def get_queryset(self):
        """Return all personality test categories."""
        return Category.objects.all()


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "polls/detail.html"


def calculate_personality(request, pk):
    category = get_object_or_404(Category, pk=pk)
    answers = []
    
    # Collect trait from each selected choice
    for question in category.questions.all():
        choice_id = request.POST.get(f"question_{question.id}")
        if choice_id:
            try:
                choice = Choice.objects.get(pk=choice_id)
                if choice.trait:
                    answers.append(choice.trait)
            except Choice.DoesNotExist:
                pass

    if not answers:
        return render(request, "polls/detail.html", {
            "category": category,
            "error_message": "Lütfen en az bir soruyu cevaplayın.",
        })

    # Find the most common trait
    most_common_trait = Counter(answers).most_common(1)[0][0]
    
    # Get the corresponding Result
    result = PersonalityResult.objects.filter(category=category, trait=most_common_trait).first()
    
    if not result:
        # Fallback if no result defined for that trait
        return HttpResponseRedirect(reverse("polls:index"))

    return HttpResponseRedirect(reverse("polls:result", args=(result.id,)))


def show_result(request, result_id):
    result = get_object_or_404(PersonalityResult, pk=result_id)
    return render(request, "polls/results.html", {"result": result})
