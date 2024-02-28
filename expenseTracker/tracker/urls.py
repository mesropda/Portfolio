from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page, contact_us, login_user, logout_user, register_user, about_us, user_profile

app_name = "tracker"

urlpatterns = [
    path('', home_page, name='home'),
    path('contact-us/', contact_us, name='contact-us'),
    path('about-us/', about_us, name='about-us'),
    path('log-in/', login_user, name='log-in'),
    path('log-out/', logout_user, name='log-out'),
    path('register/', register_user, name='register'),
    path('profile/', user_profile, name='profile')
]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA.ROOT)
