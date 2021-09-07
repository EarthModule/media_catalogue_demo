from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from movies.models import Movie


class HomePageView(TemplateView):
    template_name = "movies/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        movies = Movie.objects.all()  # .filter(cast__in=self.request.user)

        context["movies"] = movies
        return context
