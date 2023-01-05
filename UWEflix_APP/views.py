from django.shortcuts import render
from django.shortcuts import redirect
from UWEflix_APP.forms import RegisterClubForm
from UWEflix_APP.models import register_club
from django.views.generic import ListView

# Replace the existing home function with the one below
def home(request):
    return render(request, "UWEflix_APP/home.html")

def about(request):
    return render(request, "UWEflix_APP/about.html")

def contact(request):
    return render(request, "UWEflix_APP/contact.html")
    
def View_clubs(request):
    
    return render(request, "UWEflix_APP/View_clubs.html")

def register_club_page(request):
    form = RegisterClubForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect("home")
    else:
        return render(request, "UWEflix_APP/register_club_page.html", {"form": form})


class clubListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = register_club

    def get_context_data(self, **kwargs):
        context = super(clubListView, self).get_context_data(**kwargs)
        return context