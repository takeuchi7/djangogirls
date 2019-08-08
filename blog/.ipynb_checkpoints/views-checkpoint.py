from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_right(request, pk):
    return render(request, 'blog/post_right.html',)
def post_miss(request, pk):
    return render(request, 'blog/post_miss.html')
def post_right1(request, pk):
    return render(request, 'blog/post_right1.html')
def post_miss1(request, pk):
    return render(request, 'blog/post_miss1.html')
def post_right2(request, pk):
    return render(request, 'blog/post_right2.html')
def post_miss2(request, pk):
    return render(request, 'blog/post_miss2.html')
def post_right3(request, pk):
    return render(request, 'blog/post_right3.html')
def post_miss3(request, pk):
    return render(request, 'blog/post_miss3.html')
def post_right4(request, pk):
    return render(request, 'blog/post_right4.html')
def post_miss4(request, pk):
    return render(request, 'blog/post_miss4.html')
def post_right5(request, pk):
    return render(request, 'blog/post_right5.html')
def post_miss5(request, pk):
    return render(request, 'blog/post_miss5.html')
def post_right6(request, pk):
    return render(request, 'blog/post_right6.html')
def post_miss6(request, pk):
    return render(request, 'blog/post_miss6.html')
def post_right7(request, pk):
    return render(request, 'blog/post_right7.html')
def post_miss7(request, pk):
    return render(request, 'blog/post_miss7.html')
def post_right8(request, pk):
    return render(request, 'blog/post_right8.html')
def post_miss8(request, pk):
    return render(request, 'blog/post_miss8.html')
def post_right9(request, pk):
    return render(request, 'blog/post_right9.html')
def post_miss9(request, pk):
    return render(request, 'blog/post_miss9.html')
def post_right10(request, pk):
    return render(request, 'blog/post_right10.html')
def post_miss10(request, pk):
    return render(request, 'blog/post_miss10.html')
def post_right11(request, pk):
    return render(request, 'blog/post_right11.html')
def post_miss11(request, pk):
    return render(request, 'blog/post_miss11.html')
def post_right12(request, pk):
    return render(request, 'blog/post_right12.html')
def post_miss12(request, pk):
    return render(request, 'blog/post_miss12.html')
def post_right13(request, pk):
    return render(request, 'blog/post_right13.html')
def post_miss13(request, pk):
    return render(request, 'blog/post_miss13.html')
def post_right14(request, pk):
    return render(request, 'blog/post_right14.html')
def post_miss14(request, pk):
    return render(request, 'blog/post_miss14.html')
def post_right15(request, pk):
    return render(request, 'blog/post_right15.html')
def post_miss15(request, pk):
    return render(request, 'blog/post_miss15.html')
def post_right16(request, pk):
    return render(request, 'blog/post_right16.html')
def post_miss16(request, pk):
    return render(request, 'blog/post_miss16.html')
def post_right17(request, pk):
    return render(request, 'blog/post_right17.html')
def post_miss17(request, pk):
    return render(request, 'blog/post_miss17.html')
def post_right18(request, pk):
    return render(request, 'blog/post_right18.html')
def post_miss18(request, pk):
    return render(request, 'blog/post_miss18.html')
def post_right19(request, pk):
    return render(request, 'blog/post_right19.html')
def post_miss19(request, pk):
    return render(request, 'blog/post_miss19.html')