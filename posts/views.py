"""Post views """
#Django
#from django.http import HttpResponse
#from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

#Forms
from posts.forms import PostForm

#Utilities
from datetime import datetime

#Models
from posts.models import Post

""" posts = [
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
] """

# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail"""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context



# @login_required
# def create_post(request):
#     """Create new post view"""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()
    
#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )



# @login_required
# def list_posts(request):
#     """List existing post"""
#     posts = Post.objects.all().order_by('-created')
#     return render(request, 'posts/feed.html', {'posts': posts})
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