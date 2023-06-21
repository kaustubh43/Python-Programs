from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(),name='notes.details'),
    path('NotFound', views.NotFoundView.as_view(), name='NotFound')
]
