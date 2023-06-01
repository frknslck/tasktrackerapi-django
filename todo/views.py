from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer

from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class TodoView(ModelViewSet):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_fields = ['id', 'priority', 'is_done']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title'] # '__all__'

'''
    def get_queryset(self):
        # URL'den parametre değerini yakala:
        title = self.request.query_params.get('title')
        if title is None:
        # Arama yapma (parametre yok)
            return super().get_queryset()
        else:
        # Arama yap:
            # queryset içinde ara:
            return self.queryset.filter(title__contains=title)
'''