from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import EmailAttachementView


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("customer_center", views.customer_center, name="customer_center"),
    path("auto_insurance", views.auto_insurance, name="auto_insurance"),
    path("home_insurance", views.home_insurance, name="home_insurance"),
    path("business_insurance", views.business_insurance, name="business_insurance"),
    path("life_insurance", views.life_insurance, name="life_insurance"),
    path('contact', EmailAttachementView.as_view(), name='emailattachment')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
