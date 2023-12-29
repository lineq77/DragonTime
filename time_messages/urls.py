from django.urls import include, path
from .views import profile_view, year_view, month_view, day_view, hour_view, minute_view, second_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'time_messages'
urlpatterns = [
   path('', include([
       path('', profile_view, name='profile'),
       path('years/', year_view, name='years'),
       path('month/', month_view, name='month'),
       path('days/', day_view, name='days'),
       path('hours/', hour_view, name='hours'),
       path('minutes/', minute_view, name='minutes'),
       path('seconds/', second_view, name='seconds'),
   ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
