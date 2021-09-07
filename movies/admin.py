from django.contrib import admin

# Register your models here.
from movies.models import Movie, MovieStaffMember, MovieCategory, MovieRole


@admin.register(MovieCategory)
class MovieCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieStaffMember)
class MovieStaffMemberAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_alive",
        "birth_year",
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "director", "actors_list")

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("actors")

    def actors_list(self, obj):
        return ",".join(a.name for a in obj.actors.all())


@admin.register(MovieRole)
class MovieRoleAdmin(admin.ModelAdmin):
    list_display = (
        "role",
        "actor",
        "movie",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("actor", "movie")
