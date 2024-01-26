from django.shortcuts import render,redirect
from base.models import Thumbnail,Testimonial,Teacher,Post,Comment
from products.models import Product
from django.views import View 



class HomePageView(View):
    def get(self,request,*args, **kwargs):
        thumbnails=Thumbnail.objects.all()[:4]
        testimonials=Testimonial.objects.all()
        products=Product.objects.all()
        teachers=Teacher.objects.all()[:4]
        context={
            "thumbnails":thumbnails,
            "testimonials":testimonials,
            "products":products,
            "teachers":teachers
        }
        return render(request, "home/home.html",context)
    
    
    def post(self,request,*args, **kwargs):
        pass
    
class BlogListView(View):
    def get(self,request,*args, **kwargs):
        blogs=Post.objects.all()
        context={
            "blogs":blogs
        }
        return render(request,"blog/blog_list.html",context)
    
class BlogDetailView(View):
    def get(self,request,id,*args, **kwargs):
        try:
            blog=Post.objects.get(id=id)
        except:
            return redirect("blogs-list")
        
        return render(request,"blog/blog_detail.html",{"blog_data":blog})
    
    def post(self,request,id,*args, **kwargs):
        try:
            blog=Post.objects.get(id=id)
        except:
            return redirect("blogs-list")
        
        Comment.objects.create(
            
        )