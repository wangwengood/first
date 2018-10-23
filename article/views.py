from django.shortcuts import render_to_response, get_object_or_404

from .models import Article
# Create your views here.
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {}
    context['article_obj'] = article
    return render_to_response('article_detail.html', context)
def article_list(request):
    article = Article.objects.filter(is_delete=False)
    context = {}
    context['article_list'] = article
    return render_to_response('article_list.html', context)

    # try:
    #     article = Article.objects.get(id=article_id)
    # except Article.DoesNotExist:
    #     raise Http404('不存在')
    # return H
    # HttpResponse('文章标题 %s 文章内容 %s' %(article.title, article.content))