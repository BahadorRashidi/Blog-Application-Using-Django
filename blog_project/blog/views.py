from django.shortcuts import render

posts = [
    {
        'author': 'Bahador',
        'title': 'Blog Post 1',
        'content': 'First Post Contnet',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author': 'Cma',
        'title': 'Blog Post 2',
        'content': 'Second Post Contnet',
        'date_posted' : 'August 28, 2018'
    }
]



def  home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def  about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
