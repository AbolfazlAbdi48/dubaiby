from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Article


# Create your views here.
def blog_view(request):
    latest_articles = Article.published.all()[:3]
    articles = Article.published.exclude()

    context = {
        'latest_articles': latest_articles,
        'articles': articles
    }
    return render(request, 'blog/blog_list.html', context)


class BlogDetailView(DetailView):
    model = Article
    queryset = Article.published.all()
    template_name = 'blog/blog_detail.html'
