from django.shortcuts import render
from .models import Article, Profile


def show_articles(request):
    articles = Article.objects.all()

    return render(
        request,
        'articles.html',
        {'articles': articles}
    )


def show_article(request, id):
    context = {}
    if request.user.is_authenticated:
        username = request.user
        is_paid_user = Profile.objects.get(personality_id=username).paid_user
    else:
        is_paid_user = False

    try:
        article = Article.objects.get(pk=id)
        context['title'] = article.title

        if article.paid and is_paid_user == False:
            context['text'] = 'Только для платных пользователей!'
        else:
            context['text'] = article.text

    except BaseException:
        context['title'] = 'Проблема с поиском статьи!'

    return render(
        request,
        'article.html',
        context
    )
