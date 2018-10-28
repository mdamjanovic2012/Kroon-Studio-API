"""KroonStudioPDT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from kroonStudioAPI import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



schema_view = get_swagger_view(title='Kroon Studio API')
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'articles', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url('^api/', include(router.urls)),
    url('^api-doc/$', schema_view),
    url('^api-auth/', include('rest_auth.urls')),
    url('^api-auth/registration/', include('rest_auth.registration.urls')),
    url('^api-token-auth/', obtain_jwt_token, name='token_obtain_pair'),
    url('^api-token-refresh/', refresh_jwt_token, name='token_refresh'),
    url('^api-token-verify/', verify_jwt_token, name='token_verify'),
]
