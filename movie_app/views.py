from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Movie
from .forms import MovieForm
from .tasks import add


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie Added')
	    add.delay(2, 2)
        else:
            for field, error in form.errors.iteritems():
                messages.error(request, "{} : {}".format(field, error.as_text()))

            return HttpResponseRedirect(reverse("movie_app:index"))

    movie_list = Movie.objects.order_by('created_at')
    context = {'movie_list': movie_list}
    return render(request, 'index.html', context)
