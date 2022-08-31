from django.shortcuts import render
from .models import Articles, Comment
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import CommentForm, ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'News.html', {'news': news})


def news_full(request, pk):
    post = Articles.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments":comments,
        "form":form
    }

    return render(request, "News_full.html", context)

def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = ArticlesForm

    data = {
        'form': form
    }

    return render(request, 'create.html', data)

class news_update(UpdateView):
    model = Articles
    template_name = 'create.html'
    form_class = ArticlesForm

class news_delete(DeleteView):
    model = Articles
    success_url = '/News/'
    template_name = 'delete.html'
