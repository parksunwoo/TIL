from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib import messages

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save()
            messages.success(request, '새 글이 등록되었습니다.')
            return redirect(success_url)
    else :
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })

def comment_new(request, post_pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'

    # TODO : post_pk 활용
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.ip = request.META['REMOTE_ADDR']
            comment.save()
            return redirect(success_url)
    else:
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })

def post_edit(request, pk):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.error(request, '새 글을 수정/저장했습니다.')
            return redirect(success_url)
    else:
        form = form_cls(instance=post)

    return render(request, template_name, {
        'form': form,
    })


def comment_edit(request, post_pk, comment_pk):
    form_cls = CommentForm
    template_name = 'myapp/comment_form.html'
    success_url = '/'

    # TODO : post_pk 활용

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            return redirect(success_url)
    else:
        form = form_cls(instance=comment)

    return render(request, template_name, {
        'form': form,
    })
