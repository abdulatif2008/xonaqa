from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from players.views import PlayerViewSet
from matches.views import MatchViewSet
from goals.views import GoalViewSet
from contact.views import ContactMessageViewSet

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'contact', ContactMessageViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
