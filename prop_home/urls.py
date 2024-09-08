

from django.urls import path
from prop_home.views.blog import blog_details, create_blog, delete_blog, get_blogs, update_blog, all_blogs
from prop_home.views.dashboard import get_dashboard
from prop_home.views.home import about_us, contact_us, get_gallery, get_home, facility


app_name = 'prop_home'
urlpatterns = [
    path("", get_home, name="prop-home"),
    path("about-us", about_us, name="about-us"),
    path("contact-us", contact_us, name="contact-us"),
    path("gallery", get_gallery, name="get-gallery"),
    path("blogs", get_blogs, name="get-blogs"),
    path("amenities", facility, name="facility"),
    path("blogs/<slug:category_slug>", get_blogs, name="blogs-by-category"),
    path("dashboard/blogs", all_blogs, name="all-blogs"),
    path("dashboard/<username>", get_dashboard, name="get-dashboard"),
    path("dashboard/blogs/create", create_blog, name="create-blog"),
    path("dashboard/blogs/update/<slug:post_slug>", update_blog, name="update-blog"),
    path("dashboard/blogs/delete/<slug:post_slug>", delete_blog, name="delete-blog"),
    path("blogs/blog-details/<slug:blog_slug>", blog_details, name="blog-details"),
]