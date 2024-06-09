from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    print("serializer_class")
    print("I am a  good programmer....")
    authentication_class = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # for query return here
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Note.objects.filter(user=user)
        else:
            queryset = Note.objects.all()
        return queryset
