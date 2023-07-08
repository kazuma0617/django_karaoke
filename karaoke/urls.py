from django.urls import path
from .views import listfunc, detailfunc, SongCreate, PointCreate, SongDelete

urlpatterns = [
    path("list/", listfunc, name="list"),
    path("detail/<int:pk>", detailfunc, name="detail"),
    path("create/", SongCreate.as_view(), name="songcreate"),
    path("create2/", PointCreate, name="create2"),
    path("delete/<int:pk>", SongDelete.as_view(), name="delete"),
]