from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from polls.models.question import Question
from polls.models.choice import Choice


class VoteView(View):

    def post(self, request, *args, **kwargs):
        question_id = kwargs.get('pk')
        choice_id = request.GET.get('choice_id', '')
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
            return JsonResponse({'error': "Choice not found"})
        selected_choice.votes += 1
        selected_choice.save()
        return JsonResponse({"ok": True})
