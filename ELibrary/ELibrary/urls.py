from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404, handler500

#index view
def index(request):
    return render(request, 'index.html')

#dashboard view
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

#error view
def error_view(request, error_code, error_message):
    return render(request, 'error.html', {'error_code': error_code, 'error_message': error_message})

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('error/', error_view, name='error'),
    path('dashboard/', dashboard, name='dashboard'),
    path('book/', include('book.urls')),
    path('user/', include('user.urls')),
    path('borrow/', include('borrow.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)