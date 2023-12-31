from django.views import View
from django.shortcuts import render, redirect
from .form import MovieForm
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from .form import MovieSearchForm
from .models import Movie
from django.contrib.auth import logout
# Create your views here.

def display_movie_details(request, movie):
    return render(request, 'MovieDetails.html', {'movie': movie})

def movie_search(request):
    actionType = request.POST.get('action_type')
    auth_user = request.session.get('auth')
    if auth_user is not None and 'username' in auth_user:
        current_user = auth_user['username']
    UserReference_movieID = request.POST.get('movie_id')

    if request.method == 'POST' and actionType == 'search':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            search_field = form.cleaned_data['search_field']
            search_query = form.cleaned_data['search_query']

            field_mapping = {
                'MovieID': 'MovieID',
                'MovieTitle': 'MovieTitle',
                'Genre': 'Genre',
                'Director': 'Director',
                # Add other fields here
            }

            model_field = field_mapping.get(search_field)

            if model_field:
                movies = Movie.objects.filter(**{model_field: search_query})

                if movies.exists():
                    return render(request, 'Search.html', {'form': form, 'movies': movies})
                else:
                    error_message = f"No movies found with {search_field} equal to '{search_query}'."
                    return render(request, 'Search.html', {'form': form, 'error_message': error_message})

    #Button add To Favorites
    elif request.method == 'POST' and actionType == 'addMovie':

        with connection.cursor() as cursor:
            cursor.callproc('getUserID', [current_user])
            current_uID = cursor.fetchall()[0][0]
            cursor.close()

        args = [UserReference_movieID, current_uID]
        with connection.cursor() as cursor:
            cursor.callproc('addToFavorite', args)
            cursor.close()

        return HttpResponseRedirect(reverse('Movie:search'))

    #Button add To Watchlist
    elif request.method == 'POST' and actionType == 'addWatchlist':

        with connection.cursor() as cursor:
            cursor.callproc('getUserID', [current_user])
            current_uID = cursor.fetchall()[0][0]
            cursor.close()

        args = [UserReference_movieID, current_uID]
        with connection.cursor() as cursor:
            cursor.callproc('addToWatchlist', args)
            cursor.close()

        return HttpResponseRedirect(reverse('Movie:search'))

    #Button marked as watched
    elif request.method == 'POST' and actionType == 'addWatched':

        with connection.cursor() as cursor:
            cursor.callproc('getUserID', [current_user])
            current_uID = cursor.fetchall()[0][0]
            cursor.close()

        args = [UserReference_movieID, current_uID]
        with connection.cursor() as cursor:
            cursor.callproc('markWatched', args)
            cursor.close()

        return HttpResponseRedirect(reverse('Movie:search'))

    else:  # If the request method is not POST (initial page load)
        form = MovieSearchForm()
        movies = Movie.objects.all()  # Fetch all movies from the database

        return render(request, 'Search.html', {'form': form, 'movies': movies})

    return render(request, 'Search.html', {'form': form})



def index(request):
    return HttpResponse("hello world")

class MovieView(View):
    template_name = 'erwin.html'  # Corrected template_name

    def get(self, request):
        movie_form = Movie.objects.all() # Create an instance of MovieForm
        return render(request, self.template_name, {'movies': movie_form, 'form': MovieForm()})

    def post(self, request):
        movie_form = MovieForm(request.POST)  # Bind the form data
        movieID = request.POST['MovieID']
        movieTitle = request.POST['MovieTitle']
        releaseDate = request.POST['ReleaseDate']
        genre = request.POST['Genre']
        description = request.POST['Description']
        runtime = request.POST['RunTime']
        director = request.POST['Director']
        result = ""
        if movie_form.is_valid():
            cursor = connection.cursor()
            args = [movieID, movieTitle, releaseDate, genre, description, runtime, director];
            cursor.callproc('AddMovie', args)
            result = cursor.fetchall()
            cursor.close()
            return redirect('admin:Movie_movie_changelist')  # Redirect to the admin Movie change list
        return render(request, self.template_name, {'form': movie_form})

class SignOutView(View):
    def post(self, request):
        logout(request)
        return redirect('Authentication:sign-in')

def displayDetails(request):
    cursor = connection.cursor()
    cursor.callproc('displayDetails')
    result = cursor.fetchall()
    cursor.close()
    return render(request, 'actordisplay.html', {'result': result})