from django.urls import path
from UWEflix_APP import views
from UWEflix_APP.models import register_club

home_list_view = views.clubListView.as_view(
    queryset=register_club.objects.order_by("-club_rep_number")[:5],  # :5 limits the results to the five most recent
    context_object_name="club_info",
    template_name="UWEflix_APP/View_clubs.html",
)


urlpatterns = [
    path("", views.home, name="home"),
    path("club_lists", views.about, name="club_lists"),
    path("register_club_page/", views.register_club_page, name="register_club_page"),
    path("View_clubs/", home_list_view, name="View_clubs"),
    path("update_club_page/<int:pk>/", views.update_club, name="update_club"),
    path("delete_club_page/<int:pk>/", views.delete_club, name="delete_club"),

]