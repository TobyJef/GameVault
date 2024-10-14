from django.shortcuts import render


def profile(request):
    """ Displays the User's profile """
    template ='profiles/profile.html'
    context = {}

    return render(request, template, context)

