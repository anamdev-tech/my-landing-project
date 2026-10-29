import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages  # 🎯 নতুন ইম্পোর্ট
from .models import Lead  

# ১. ল্যান্ডিং পেজ এবং অটো-ইমেইল ভিউ (উপায় ১ অনুযায়ী সম্পূর্ণ আপডেট করা)
def landing_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # ডাটাবেজে ডেটা সেভ করা
        lead = Lead.objects.create(name=name, email=email)
        
        # অটোমেটিক ইমেইল পাঠানোর লজিক
        subject = 'Welcome to our platform!'
        message = f'Hi {name},\n\nThank you for connecting with us through our landing page. We will get back to you soon!'
        from_email = 'webmaster@localhost'
        recipient_list = [email]
        
        send_mail(subject, message, from_email, recipient_list)
        
        # 🎯 সাকসেস মেসেজ সেট করা
        messages.success(request, 'আপনার তথ্য সফলভাবে জমা হয়েছে!')
        
        # 🎯 পেজটি রিফ্রেশ করে আবার ফাঁকা ফর্মে ফিরিয়ে নেওয়া
        return redirect('landing_page')  
        
    return render(request, 'lead_collector/index.html') 

# ২. ডাটাবেজের ডেটা CSV আকারে ডাউনলোড করার ভিউ (এটি আগের মতোই থাকবে)
def export_leads_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="landing_page_leads.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Email'])

    leads = Lead.objects.all()
    for lead in leads:
        writer.writerow([lead.id, lead.name, lead.email])

    return response