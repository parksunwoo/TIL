from Django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Django.shortcuts import render, redirect, get_object_or_404
from Django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from .models import Post, Comment
from Django.contrib import messages

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

# def post_new(request):
#     form_cls = PostForm
#     template_name = 'myapp/post_form.html'
#     success_url = '/'
#
#     if request.method == 'POST':
#         form = form_cls(request.POST, request.FILES)
#         if form.is_valid():
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             messages.success(request, '새 글이 등록되었습니다.')
#             return redirect(success_url)
#     else :
#         form = form_cls()
#
#     return render(request, template_name, {
#         'form': form,
#     })

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # template_name = 'myapp/post_form.html'

    # model만을 활용했을 떄
    # model = Post
    # fields = '__all__'

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, '새 글을 저장했습니다')

post_new = PostCreateView.as_view()

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, '글을 수정/ 저장했습니다')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'myapp/post_confirm_delete.html', {
        'post':post,
    })

# post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('post_list'))



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
            messages.success(request, '새 댓글이 등록되었습니다.')
            return redirect(success_url)
    else:
        form = form_cls()

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
            messages.debug(request, '댓글을 수정/저장했습니다.')
            return redirect(success_url)
    else:
        form = form_cls(instance=comment)

    return render(request, template_name, {
        'form': form,
    })


from rest_framework.generics import ListCreateAPIView
from .serializers import PostSerializer
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list_create = PostListCreateAPIView.as_view()