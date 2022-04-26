from django.shortcuts import render


def home_page(request):
    return render(request, 'music_talks_blog/blog_home_page.html')
