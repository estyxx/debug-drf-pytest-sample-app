from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from polls.models import Question
from polls.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # questo e' l'errore che dovrebbe dare eccezione
        request.data["id"] = "AttributeError"

        return Response("ok", status=status.HTTP_201_CREATED)
