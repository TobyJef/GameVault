from django.shortcuts import render

#Code Snippet from Boutique Ado - Adding a custom 404 page
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)