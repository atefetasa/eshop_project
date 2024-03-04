from django.shortcuts import render
from django.views import View
from .models import Article
from django.views.generic.list import ListView


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles':articles
#         }
#         return render(request, 'article_module/articles_page.html', context)


class ArticleListView(ListView):
    model = Article
    template_name = 'article_module/articles_page.html'
    paginate_by = 5