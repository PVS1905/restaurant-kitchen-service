from django.urls import path
from .views import index, DishTypeListView, DishListView, CookListView, DishDetailView, DishCreateView, DishUpdateView, \
    toggle_assign_to_dish, DishDeleteView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, CookDetailView, \
    CookCreateView, CookDeleteView, CookYearsExperienceUpdateView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes_type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dishes_type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dishes_type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dishes_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/<int:pk>/toggle-assign/",
         toggle_assign_to_dish,
         name="toggle-dish-assign",
    ),
    path(
    "cooks/",
    CookListView.as_view(),
    name="cook-list",
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookYearsExperienceUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]
app_name = "kitchen"