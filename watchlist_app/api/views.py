from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Movies
from .serializers import MovieSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):

    if request.method == 'GET':
        movie = Movies.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    
    elif request.method == 'DELETE':
        pass
    
    