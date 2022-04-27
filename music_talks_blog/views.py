from django.shortcuts import render


def home_page(request):
    return render(request, 'music_talks_blog/home_page.html')
