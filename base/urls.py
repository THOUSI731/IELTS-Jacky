from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomePageView.as_view(),name="home-view"),
    path("blogs/",views.BlogListView.as_view(),name="blogs-list"),
    path("blog/<int:id>/",views.BlogDetailView.as_view(),name="blog_detail"),
    path("enroll/<int:id>/",views.CourseEnrollCreateView.as_view(),name="course_enroll")
]

