from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Movies
from .serializers import MovieSerializer
from django.http import JsonResponse

@api_view()
def movie_list(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movies.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)