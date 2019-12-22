from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def post_new(request):
    form_cls = PostForm
    template_name = 'myapp/post_form.html'
    success_url = '/'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            # post.save()
            return redirect(success_url)
    else :
        form = form_cls()

    return render(request, template_name, {
        'form': form,
    })