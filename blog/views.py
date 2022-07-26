from datetime import datetime
from django.shortcuts import get_object_or_404, render
from .models import Post, Skill
import requests

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

def repositories(request):
    repositories_display = []
    username = 'johnnyfers'
    url = f'https://api.github.com/users/{username}/repos'

    response = requests.get(url)
    repositories = list(response.json())
    repositories.sort(key=lambda x: datetime.strptime(x['created_at'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True)
    for repo in repositories:
        skill_language = None
        try:
            skill = Skill.objects.get(name=repo['language'].lower())
            skill_language = skill
        except:
            skill_language = None
        repositories_display.append({
            'name': repo['name'].replace('-', ' '),
            'description': repo['description'],
            'url': repo['html_url'],
            'language_image': skill_language,
            'owner_avatar': repo['owner']['avatar_url'],
        })
    
    return render(request, 'blog/all_repositories.html', {
        'repositories': repositories_display
    })