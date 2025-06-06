from .forms import SerchForm

def search_form(request):
    return {'searchform':SerchForm()}