from django.urls import path
from .views import index, DishTypeListView, DishListView, CookListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_type/",
        DishTypeListView.as_view(),
        name="dish_type_list",
    ),
    path(
        "dish/",
        DishListView.as_view(),
        name="dish_list",
    ),
    path(
    "cook/",
    CookListView.as_view(),
    name="cook_list",
    ),
]
app_name = "kitchen"