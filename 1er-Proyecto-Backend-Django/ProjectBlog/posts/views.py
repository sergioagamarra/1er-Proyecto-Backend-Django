from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, Category
from django.db.models import Count
import json


# Create your views here.

def home(request):
    return redirect("/posts")


def posts(request):
    posts = Post.objects.all().order_by("-created_date", "-id")   # SELECT * FROM posts
    categories = Category.objects.all()
    #posts = Post.objects.filter(title__icontains="Publicación") # SELECT * FROM posts WHERE title LIKE "Publicación"

    return render(request, 'posts/posts.html', {
        'posts': posts,
        'categories': categories
         })


def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post.id)

    return render(request, 'posts/post.html', {
        'post': post,
        'comments': comments,
        'cant_comments': len(comments)
        })


def create_post(request):
    if request.method == "POST":
        id_category = request.POST['category']
        category = Category.objects.get(id=id_category)
        post = Post(
            title = request.POST['title'],
            description = request.POST['description'],
            img = request.POST['image'],
            content = request.POST['content'],
            category = category,
            author=request.user
        )

        post.save()

        return redirect("/posts")

    categories = Category.objects.all()
    return render(request, 'posts/create.html', {
        'categories': categories
        })


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        id_category = request.POST['category']
        category = Category.objects.get(id=id_category)
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.img = request.POST['image']
        post.content = request.POST['content']
        post.category = category


        post.save()

        return redirect("/posts")
    categories = Category.objects.all()
    return render(request, 'posts/edit.html', {
        'post': post,
        'categories': categories
        })


def delete_post(request,id):
    post = Post.objects.get(id=id)

    post.delete()
    return redirect("/posts")

def search_post(request):
    if request.method == "POST":
        search = request.POST['search']
        posts = Post.objects.filter(title__icontains = search).order_by("-created_date", "-id") # SELECT * FROM posts WHERE title LIKE "Publicación"
        categories = Category.objects.all()

    return render(request, 'posts/posts.html', {
        'posts': posts,
        'categories': categories
         })

def category_post(request, id):
    posts = Post.objects.filter(category=id)
    categories = Category.objects.all()

    return render(request, 'posts/posts.html', {
        'posts': posts,
        'categories': categories
        })

def create_comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        comment = Comment(
            post = post,
            content = request.POST['comment'],
            user = request.user
        )

        comment.save()

        return redirect("/posts/" + str(post.id))

    return redirect('/posts')

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    id_post = comment.post.id
    comment.delete()

    return redirect('/posts/' + str(id_post))
  
