from django.shortcuts import render
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def profile_view(request):
  return render(request, 'time_messages/profile.html')

def year_view(request):
  today = dt.today()
  old_date = dt.strptime('2012-09-17', '%Y-%m-%d')
  diff = relativedelta(today, old_date)
  years = diff.years
  context = {'years': years}
  return render(request, 'time_messages/years.html', context)

def month_view(request):
 today = dt.today()
 old_date = dt.strptime('2012-09-17', '%Y-%m-%d')
 diff = relativedelta(today, old_date)
 years = diff.years
 months = diff.months
 total_months = years * 12 + months
 context = {'total_months': total_months}
 return render(request, 'time_messages/month.html', context)

def day_view(request):
 today = dt.today()
 old_date = dt.strptime('2012-09-17', '%Y-%m-%d')
 diff = relativedelta(today, old_date)
 years = diff.years
 days = diff.days
 total_days = years * 365 + days
 context = {'total_days': total_days}
 return render(request, 'time_messages/days.html', context)

def hour_view(request):
 today = dt.today()
 old_date = dt.strptime('2012-09-17', '%Y-%m-%d')
 diff = relativedelta(today, old_date)
 years = diff.years
 hours = diff.hours
 total_hours = years * 365 * 24 + hours
 context = {'total_hours': total_hours}
 return render(request, 'time_messages/hours.html', context)

def minute_view(request):
 today = dt.today()
 old_date = dt.strptime('2012-09-17', '%Y-%m-%d')
 diff = relativedelta(today, old_date)
 years = diff.years
 minutes = diff.minutes
 total_minutes = years * 365 * 24 * 60 + minutes
 context = {'total_minutes': total_minutes}
 return render(request, 'time_messages/minutes.html', context)

def second_view(request):
 today = dt.today()
 old_date = dt.strptime('2012-09-17', '%Y-%m-%d')
 diff = relativedelta(today, old_date)
 years = diff.years
 seconds = diff.seconds
 total_seconds = years * 365 * 24 * 60 * 60 + seconds
 context = {'total_seconds': total_seconds}
 return render(request, 'time_messages/seconds.html', context)