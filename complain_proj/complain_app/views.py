from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status, viewsets
from rest_framework.decorators import action

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['GET'])
    def get_complains(self, request):
        query = request.query_params.get('id')
        if query is None:
            return Response({'message':'Ошибка ничего не найдено'}, status=status.HTTP_404_NOT_FOUND)
        complain = Complain.objects.filter(written_by=query)
        serializer = ComplainSerializer(complain, many=True)
        return Response(serializer.data)
    
class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
# Create your views here.
