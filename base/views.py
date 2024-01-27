from django.shortcuts import render, redirect
from base.models import Thumbnail, Testimonial, Teacher, Post, Comment, EnrollCourse
from products.models import Product
from django.views import View
from base.forms import EnrollNowForm
from django.contrib import messages


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        thumbnails = Thumbnail.objects.all()[:4]
        testimonials = Testimonial.objects.all()
        courses = Product.objects.all()
        teachers = Teacher.objects.all()[:4]
        form = EnrollNowForm()
        context = {
            "thumbnails": thumbnails,
            "testimonials": testimonials,
            "courses": courses,
            "teachers": teachers,
            "form": form,
        }
        return render(request, "home/home.html", context)

    def post(self, request, *args, **kwargs):
        pass


class CourseEnrollCreateView(View):
    def post(self, request, id, *args, **kwargs):
        forms = EnrollNowForm(request.POST)
        if forms.is_valid():
            try:
                course = Product.objects.get(id=id)
            except Product.DoesNotExist:
                messages.error(request, "Course not found")
                return redirect("home-view")
            full_name = forms.cleaned_data.get("full_name", None)
            email = forms.cleaned_data.get("email", None)
            phone_number = forms.cleaned_data.get("phone_number", None)
            EnrollCourse.objects.create(
                course=course,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
            )
            messages.success(
                request, "Form Submitted Successfully.We Will Contact You Soon"
            )
            return redirect("home-view")
        messages.error(request,"Something Went Wrong")
        return redirect("home-view")


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

        return render(request, "blog/blog_detail.html", {"blog_data": blog})

    def post(self, request, id, *args, **kwargs):
        try:
            blog = Post.objects.get(id=id)
        except:
            return redirect("blogs-list")

        Comment.objects.create()
