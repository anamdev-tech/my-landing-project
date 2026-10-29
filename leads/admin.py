from django.contrib import admin
from .models import Lead

# অ্যাডমিন প্যানেলে কলামগুলো সুন্দরভাবে সাজিয়ে দেখানোর জন্য
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at') # এই ৩টি কলাম ড্যাশবোর্ডে দেখাবে
    search_fields = ('name', 'email')             # নাম বা ইমেল দিয়ে সার্চ করার বক্স থাকবে

admin.site.register(Lead, LeadAdmin)