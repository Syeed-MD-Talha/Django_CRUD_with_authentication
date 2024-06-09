from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# ......................List of posts...................
def PostView(request):
    data=Post.objects.all()
    return render(request,'post_view.html',{'posts':data})



#.......................... Create new post.............................
#@login_required
def PostCreate(request):
    if request.method=='POST':
        print("================= POST ====================")
        info=PostForm(request.POST)
        if info.is_valid():
            print(info.cleaned_data)
            info.save()
            return redirect('../')
        else:
            return render(request,'create_post.html',{'form':info})
        
    else:
        print("=================  GET =================")
        context=PostForm()
        return render(request,'create_post.html',{'form':context})


#................... Edit Post .................................

from django.shortcuts import get_object_or_404
def edit_post(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=='GET':
        context={'form':PostForm(instance=post),'id':id}
        return render(request,'edit_post.html',context)
    
    elif request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post')
        else:
            return render(request,'edit_post.html',{'form':form})


#............................ Delete Post .............................

def delete_post(request,id):
    post=get_object_or_404(Post,id=id)
    context={'post':post}

    if request.method=='GET':
        return render(request,'delete_post.html',context)
    
    elif request.method=='POST':
        post.delete()
        return redirect('view_post')