from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name="detail"),
    path("category/<int:pk>/calculate/", views.calculate_personality, name="calculate"),
    path("result/<int:result_id>/", views.show_result, name="result"),
]
