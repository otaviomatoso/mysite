from django.urls import path
from polls_api.views.hello_world_view import HelloWorldView
from django.views.decorators.csrf import csrf_exempt
from polls_api.views.question_view import QuestionView
from polls_api.views.vote_view import VoteView
from polls_api.views.results_view import ResultsView

app_name = 'polls_api'

urlpatterns = [
    # path('', HelloWorldView.as_view(), name='hello-world'),
    path('questions/', csrf_exempt(QuestionView.as_view()), name='questions'),
    path('questions/<int:pk>', csrf_exempt(QuestionView.as_view()), name='question'),
    path('questions/<int:pk>/vote', csrf_exempt(VoteView.as_view()), name='vote'),
    path('questions/<int:pk>/results', csrf_exempt(ResultsView.as_view()), name='results'),
]

