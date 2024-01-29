from django.shortcuts import render, redirect
from base.models import Thumbnail, Testimonial, Teacher, Post, Comment, EnrollCourse
from products.models import Product
from django.views import View
from base.forms import EnrollNowForm
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        thumbnails = Thumbnail.objects.all()[:4]
        testimonials = Testimonial.objects.all()
        courses = Product.objects.all()
        teachers = Teacher.objects.all()[:4]
        blogs = Post.objects.prefetch_related("blog_comments").all().order_by("-id")[:2]
        form = EnrollNowForm()
        context = {
            "thumbnails": thumbnails,
            "testimonials": testimonials,
            "courses": courses,
            "teachers": teachers,
            "form": form,
            "blogs": blogs,
        }
        return render(request, "home/home.html", context)

class CourseEnrollCreateView(View):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(id=id)
        serialized_product = {
            "id": product.pk,
            "product_name": product.product_name,
            "image": str(product.image),
            "price": product.price,
            "description": product.description,
            "has_offer": product.has_offer,
        }
        return JsonResponse({"data": serialized_product})

    def post(self, request, id, *args, **kwargs):
        forms = EnrollNowForm(request.POST)
        if forms.is_valid():
            try:
                course = Product.objects.get(id=id)
            except Product.DoesNotExist:
                messages.error(request, "Course not found")
                return redirect("home-view")
            EnrollCourse.objects.create(
                course=course,
                full_name=forms.cleaned_data.get("full_name", None),
                email=forms.cleaned_data.get("email", None),
                phone_number=forms.cleaned_data.get("phone_number", None),
            )
            return JsonResponse({"message":"Form Submitted Successfully","success":True,"status":201})
        return JsonResponse({"errors":forms.errors,"success":False,"status":400})


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        blogs = Post.objects.all()
        context = {"blogs": blogs}
        return render(request, "blog/blog_list.html", context)


class BlogDetailView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            blog = Post.objects.get(id=id)
        except:
            return redirect("blogs-list")
        blogs = Post.objects.exclude(id=id)
        return render(
            request, "blog/blog_detail.html", {"blog_data": blog, "blogs": blogs}
        )

    def post(self, request, id, *args, **kwargs):
        print(request, "nokkam")
        try:
            blog = Post.objects.get(id=id)
        except:
            return redirect("blogs-list")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        message = request.POST.get("message")
        Comment.objects.create(
            post=blog,
            full_name=full_name,
            email=email,
            message=message,
            website=website,
        )
        return redirect(reverse("blog_detail", kwargs={"id": id}))


# class StayInTouchView(View):
#     def post(self, request, *args, **kwargs):
#         full_name = request.POST.get("first_name")
#         email = request.POST.get("last_name")
#         website = request.POST.get("website")
#         message = request.POST.get("message")
#         Comment.objects.create(
#             post=blog,
#             full_name=full_name,
#             email=email,
#             message=message,
#             website=website,
#         )
#         return redirect("home-view")
