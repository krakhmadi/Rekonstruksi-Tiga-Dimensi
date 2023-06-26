from django.urls import path
from .views import HomeView, PageDetailView, PostView , detail, SearchView, DeletePostView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.index, name='index'),
    path('', HomeView.as_view(), name='home'),
    # path('detail/<int:pk>', PageDetailView.as_view(), name='detail'),
    path('detail/<int:id>', detail, name='detail'),
    path('post/', PostView.as_view(), name='post'),
    # path('process/', ProcessView.as_view(), name='process'),
    path('search/', SearchView.as_view(), name='search'),
    path('detail/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
