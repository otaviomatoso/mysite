from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import View
from polls.models.question import Question
from polls.models.choice import Choice

import json


class QuestionView(View):

    def get(self, request, *args, **kwargs):
        if kwargs:
            question_id = kwargs.get('pk')
            # question = Question.objects.filter(id=question_id).values()
            question = get_object_or_404(Question, pk=question_id)
            return JsonResponse(list(question), safe=False)
        questions = Question.objects.values()
        return JsonResponse(list(questions), safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        question_text = body.get('question')
        choices = body.get('choices')
        question = Question(question_text=question_text, pub_date=timezone.now())
        question.save()
        for choice in choices:
            question.choice_set.create(choice_text=choice, votes=0)
        return JsonResponse({'id': question.id})
