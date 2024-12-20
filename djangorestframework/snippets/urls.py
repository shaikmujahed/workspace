from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')


# The API urls now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]




# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
# from rest_framework import renderers
# from snippets.views import api_root, SnippetViewSet, UserViewSet

# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get':'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = UserViewSet.as_view({
#     'get':'list'
# })

# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])