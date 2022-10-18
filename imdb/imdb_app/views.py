# import json
# from django.http import JsonResponse
# from imdb_app.models import Movie
# # Create your views here.


# def movie_list(request):
#     movies = Movie.objects.all()

#     # converting queryset into an iterable and then assigning it in a dict so that JsonResponse can send it
#     data = list(movies.values())
#     return JsonResponse(data, safe=False)

# # movie/list/1  -> 1 is pk
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
    
#     data = {
#         'name' : movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     print(data)
    
#     return JsonResponse(data)