from django.shortcuts import get_object_or_404, render
from .models import Post, Skill


def get_date(post):
    return post['date']


def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    skills = Skill.objects.all()

    return render(request, 'blog/index.html', {
        'posts': latest_posts,
        'skills': skills
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all_posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'tags': post.tags.all()
    })
