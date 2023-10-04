from django.contrib import admin
from django.urls import path
from introduction_to_django_overview_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("post/<int:year>/", views.year_archive, name="year_archive"),
    path("post/<int:year>/<int:month>/", views.month_archive, name="month_archive"),
    path("post/<int:year>/<int:month>/<int:pk>/", views.post_detail, name="post_detail"),
]