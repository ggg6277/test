from django.shortcuts import render

from .forms import CommentForm
from .models import Contents, Comment
# Create your views here.
def base(request):
    return render(request, 'base.html')

def base1(request):
    contents = Contents.objects.all()
    context = {
        "contents" : contents,
    }
    return render(request, 'base1.html', context)

def blog(request):
    contents = Contents.objects.all()
    context = {
        "contents":contents,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, pk):
    print("value is %d"%pk)
    contents = Contents.objects.get(pk = pk)
    comments = Comment.objects.filter(contents = contents)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                contents = contents,
            )
            comment.save()
        context ={
            "contents":contents,
            "comments":comments,
            "form":form
        }
        return render(request, "blog_detail.html", context)
    else:
        form = CommentForm()
        context ={
            "contents":contents,
            "comments":comments,
            "form":form
        }
        return render(request, "blog_detail.html", context)