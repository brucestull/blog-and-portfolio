from django.shortcuts import render, redirect

from config.settings.common import THE_SITE_NAME
from blog.models import Post, Comment
from blog.forms import CommentForm


def blog_index(request):
    """
    View for the `blog.Blog` list view.
    """
    posts = Post.objects.all().order_by("-date_posted")
    context = {
        "the_site_name": THE_SITE_NAME,
        "page_title": "Knappings",
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)


def blog_category(request, category):
    """
    View for the `blog.Blog` list view filtered by `category`.
    """
    posts = Post.objects.filter(categories__name__icontains=category).order_by(
        "-date_posted"
    )
    context = {
        "the_site_name": THE_SITE_NAME,
        "page_title": "Knappings",
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    """
    View for the `blog.Blog` detail view.
    """
    post = Post.objects.get(pk=pk)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return redirect("blog:blog-detail", pk=post.pk)

    comments = Comment.objects.filter(post=post)
    context = {
        "the_site_name": THE_SITE_NAME,
        "page_title": "Knappings",
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/blog_detail.html", context)
