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
def post_right20(request, pk):
    return render(request, 'blog/post_right20.html')
def post_miss20(request, pk):
    return render(request, 'blog/post_miss20.html')
def post_right21(request, pk):
    return render(request, 'blog/post_right21.html')
def post_miss21(request, pk):
    return render(request, 'blog/post_miss21.html')
def post_right22(request, pk):
    return render(request, 'blog/post_right22.html')
def post_miss22(request, pk):
    return render(request, 'blog/post_miss22.html')
def post_right23(request, pk):
    return render(request, 'blog/post_right23.html')
def post_miss23(request, pk):
    return render(request, 'blog/post_miss23.html')
def post_right24(request, pk):
    return render(request, 'blog/post_right24.html')
def post_miss24(request, pk):
    return render(request, 'blog/post_miss24.html')
def post_right25(request, pk):
    return render(request, 'blog/post_right25.html')
def post_miss25(request, pk):
    return render(request, 'blog/post_miss25.html')
def post_right26(request, pk):
    return render(request, 'blog/post_right26.html')
def post_miss26(request, pk):
    return render(request, 'blog/post_miss26.html')
def post_right27(request, pk):
    return render(request, 'blog/post_right27.html')
def post_miss27(request, pk):
    return render(request, 'blog/post_miss27.html')
def post_right28(request, pk):
    return render(request, 'blog/post_right28.html')
def post_miss28(request, pk):
    return render(request, 'blog/post_miss28.html')
def post_right29(request, pk):
    return render(request, 'blog/post_right29.html')
def post_miss29(request, pk):
    return render(request, 'blog/post_miss29.html')
def post_right30(request, pk):
    return render(request, 'blog/post_right30.html')
def post_miss30(request, pk):
    return render(request, 'blog/post_miss30.html')
def post_right31(request, pk):
    return render(request, 'blog/post_right31.html')
def post_miss31(request, pk):
    return render(request, 'blog/post_miss31.html')
def post_right32(request, pk):
    return render(request, 'blog/post_right32.html')
def post_miss32(request, pk):
    return render(request, 'blog/post_miss32.html')
def post_right33(request, pk):
    return render(request, 'blog/post_right33.html')
def post_miss33(request, pk):
    return render(request, 'blog/post_miss33.html')
def post_right34(request, pk):
    return render(request, 'blog/post_right34.html')
def post_miss34(request, pk):
    return render(request, 'blog/post_miss34.html')
def post_right35(request, pk):
    return render(request, 'blog/post_right35.html')
def post_miss35(request, pk):
    return render(request, 'blog/post_miss35.html')
def post_right36(request, pk):
    return render(request, 'blog/post_right36.html')
def post_miss36(request, pk):
    return render(request, 'blog/post_miss36.html')
def post_right37(request, pk):
    return render(request, 'blog/post_right37.html')
def post_miss37(request, pk):
    return render(request, 'blog/post_miss37.html')
def post_right38(request, pk):
    return render(request, 'blog/post_right38.html')
def post_miss38(request, pk):
    return render(request, 'blog/post_miss38.html')
def post_right39(request, pk):
    return render(request, 'blog/post_right39.html')
def post_miss39(request, pk):
    return render(request, 'blog/post_miss39.html')
def post_right40(request, pk):
    return render(request, 'blog/post_right40.html')
def post_miss40(request, pk):
    return render(request, 'blog/post_miss40.html')
def post_right41(request, pk):
    return render(request, 'blog/post_right41.html')
def post_miss41(request, pk):
    return render(request, 'blog/post_miss41.html')
def post_right42(request, pk):
    return render(request, 'blog/post_right42.html')
def post_miss42(request, pk):
    return render(request, 'blog/post_miss42.html')
def post_right43(request, pk):
    return render(request, 'blog/post_right43.html')
def post_miss43(request, pk):
    return render(request, 'blog/post_miss43.html')
def post_right44(request, pk):
    return render(request, 'blog/post_right44.html')
def post_miss44(request, pk):
    return render(request, 'blog/post_miss44.html')
def post_right45(request, pk):
    return render(request, 'blog/post_right45.html')
def post_miss45(request, pk):
    return render(request, 'blog/post_miss45.html')
def post_right46(request, pk):
    return render(request, 'blog/post_right46.html')
def post_miss46(request, pk):
    return render(request, 'blog/post_miss46.html')
def post_right47(request, pk):
    return render(request, 'blog/post_right47.html')
def post_miss47(request, pk):
    return render(request, 'blog/post_miss47.html')
def post_right48(request, pk):
    return render(request, 'blog/post_right48.html')
def post_miss48(request, pk):
    return render(request, 'blog/post_miss48.html')
def post_right49(request, pk):
    return render(request, 'blog/post_right49.html')
def post_miss49(request, pk):
    return render(request, 'blog/post_miss49.html')