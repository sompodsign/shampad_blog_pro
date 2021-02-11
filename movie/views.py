from django.shortcuts import render, redirect
from .movie_recommender import movie_list_creator, trailer_finder, poster_finder, movie_list, randomizer
from .movie_dialoge_generater import quotes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MovieForm, EditForm
import random
from .models import Movie
from django.contrib.auth.decorators import login_required


def watch_now(request):
    quote = random.choice(quotes)
    random_movie = random.choice(movie_list)
    random_movie['poster'] = poster_finder(random_movie)
    random_movie['trailer'] = trailer_finder(random_movie)
    return render(request, 'movie/watch_now.html', {
        'movie': random_movie,
        'quote': quote,
    })


def custom_filter(request):
    quote = random.choice(quotes)
    if request.method == "POST":
        if 'movies' in request.session:
            del request.session['movies']
        request.session['from_year'] = request.POST['from-year']
        request.session['to_year'] = request.POST['to-year']
        try:
            request.session['genre'] = request.POST['genre']
        except:
            request.session['genre'] = ''
        request.session['from_rating'] = request.POST['from-rating']
        request.session['to_rating'] = request.POST['to-rating']
        custom_movie_list = movie_list_creator(request.session['from_year'],
                                               request.session['to_year'],
                                               request.session['genre'],
                                               request.session['from_rating'],
                                               request.session['to_rating'],
                                               )
        request.session['movies'] = custom_movie_list
    try:
        x_movie_list = request.session['movies']
    except KeyError:
        x_movie_list = movie_list
    try:
        start, end = randomizer(request.session['movies'])
    except KeyError:
        start, end = randomizer(movie_list)
    new_list = []
    for movie in x_movie_list[start:end]:
        movie['poster'] = poster_finder(movie)
        movie['trailer'] = trailer_finder(movie)
        new_list.append(movie)
    return render(request, 'movie/custom-filter.html', {'movies': new_list,
                                                        'quote': quote,
                                                        })


@login_required
def add_item(request):  # add new media
    quote = random.choice(quotes)
    user = request.user
    if request.method == "POST":
        path = request.POST.get('path')
        if not path:
            # if the add request is from add item page.
            form = MovieForm(request.POST)
            if form.is_valid():
                new_item = form.save(commit=False)
                new_item.author = user
                new_item.save()
                return redirect('movie:movie_library')
        else:
            # if the request is direct from the watch now or custom filter page.
            title = request.POST['title']
            image_url = request.POST['img_url']
            # year = request.POST['year']
            rating = request.POST['rating']
            new_item = Movie(title=title, img_url=image_url,
                             rating=rating, author=user,
                             watch="To watch")
            new_item.save()
            return redirect(path)
    return render(request, 'movie/add_movie.html',
                  context={'form': MovieForm(),
                           'quote': quote})


@login_required
def movie_library(request):  # movie library
    user = request.user
    quote = random.choice(quotes)
    movies = Movie.objects.filter(author=user, active=True)
    # paginator = Paginator(movies, 12)
    # page = request.GET.get('page')
    # try:
    #     movies = paginator.page(page)
    # except PageNotAnInteger:
    #     movies = paginator.page(1)
    # except EmptyPage:
    #     movies = paginator.page(paginator.num_pages)
    return render(request, 'movie/library/list.html', {'movies': movies,
                                                       'quote': quote,
                                                       # 'page': page,
                                                       'total': len(movies),
                                                       })


@login_required
def edit_item(request, id):
    movie = Movie.objects.get(pk=id)
    data = {'title': movie.title,
            'img_url': movie.img_url,
            'watch': movie.watch,
            'active': movie.active}
    form = EditForm(initial=data)
    if request.user == movie.author:
        if request.method == "POST":
            form = EditForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                movie.title = cd['title']
                movie.img_url = cd['img_url']
                movie.watch = cd['watch']
                movie.active = cd['active']
                movie.save()
                return redirect('movie:movie_library')
    return render(request, 'movie/edit_movie.html',
                  {'form': form,
                   'id': movie.id})


@login_required
def delete_item(request, id):
    movie = Movie.objects.get(pk=id)
    if request.user == movie.author:
        movie.delete()
        return redirect('movie:movie_library')
