from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.split if hasattr(admin.site, 'split') else admin.site.urls),
    path('', include('leads.urls')), # এই লাইনটি আমাদের অ্যাপের ইউআরএলকে মেইন প্রজেক্টের সাথে যুক্ত করবে
]