from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
     PageNotAnInteger
from django.views.generic import ListView

# Create your views here.
def post_list(request):
    post = Post.published.all()
    return render(request, 'main/post/list.html',
                    {'posts':'posts'}) 


def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status = 'published', published__year = year, publised__month = month, published__day = day)

    return render(request,
        'main/detail.html',
        {'post': post})



def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
     posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
     posts = paginator.page(paginator.num_pages)
    return render(request,
    'blog/post/list.html',
    {'page': page,
    'posts': posts})




class PostListView(ListView):
 queryset = Post.published.all()
 context_object_name = 'posts'
 paginate_by = 3
 template_name = 'main/list.html'

