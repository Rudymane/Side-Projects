from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import EmailAttachementView


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('contact', EmailAttachementView.as_view(), name='emailattachment')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
