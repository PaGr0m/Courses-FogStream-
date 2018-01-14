from django.contrib import admin
from .models import Album, Genre, Musician, Song


class DiscographyAdmin(admin.ModelAdmin):
    list_display = ["song", "musician", "album", "genre"]
    list_filter = ["musician", "album",]
    search_fields = ["song",]

    # list_display = [field.name for field in Song._meta.fields]

    class Meta:
        model = Song


admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Musician)
admin.site.register(Song, DiscographyAdmin)

# admin.site.register(DiscographyAdmin)