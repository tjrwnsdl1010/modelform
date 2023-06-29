from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:index')
    else:
        return render(request, 'articles/create.html')
    
def detail(request,id):
    article = Article.objects.get(id=id)
    context = {
        'article' : article,
    }

    return render(request, 'articles/detail.html',context)

def create2(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
        
    else:
        form = ArticleForm()

    context = {
        'form':form,
    }
    return render(request, 'articles/form.html',context)

def update(request,id):
    article = Article.objects.get(id=id)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.id)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def delete(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')