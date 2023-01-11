from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import View
from polls.models.question import Question
from polls.models.choice import Choice

import json


class ResultsView(View):

    def get(self, request, *args, **kwargs):
        question_id = kwargs.get('pk')
        question = get_object_or_404(Question, pk=question_id)
        choices = question.choice_set.all()
        results = {}
        for choice in choices:
            results.update({choice.choice_text: choice.votes})
        response = {"question": question.question_text, "results": results}
        return JsonResponse(response)
