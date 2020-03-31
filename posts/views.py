"""Post views """
#Django
#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yesica Cortez',
            'picture': 'https://picsum.photos/60/60/?image=1027',

        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036',

    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/60/60/?image=1005'

        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/60/60/?image=883'

        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1076',
    }
]

# Create your views here.

@login_required
def list_posts(request):
    """List existing post"""
    print(posts)
    return render(request, 'posts/feed.html', {'posts': posts})
    # content = []
    # i = 0
    # content.append("""
    #         <p><strong>{name}</strong></p>
    #         <p><small>{user} - <i>{timestamp}</i></small></p>
    #         <figure><img src="{picture}"/></figure>
    #     """.format(**post))
    # for post in posts:
    #     i += 1
    # print(i)
    # return HttpResponse('<br>'.join(content))

