from django.urls import path
from . import views
urlpatterns = [
    path("", views.print_hello, name="print_hello"),
    path("azamat", views.azamat, name="azamat"),
    path("akmal", views.akmal, name="akmal"),
    path("<str:name>", views.greet, name="greet")

]