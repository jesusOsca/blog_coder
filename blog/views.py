from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        comentario_form = ComentarioForm()
    return render(request, 'blog/blog_detail.html', {'post': post, 'comentarios': comentarios, 'comentario_form': comentario_form})

def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = PostForm()
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})
