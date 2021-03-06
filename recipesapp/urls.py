from django.urls import include, re_path, path
from recipesapp import views

app_name = 'recipesapp'

urlpatterns = [
    path('all/', views.RecipesAll.as_view(), name='all'),
    path('all/<int:typeof>/', views.RecipesAll.as_view(), name='all'),
    path(r'my/', views.RecipesMy.as_view(), name='my'),
    path(r'my/<int:typeof>/', views.RecipesMy.as_view(), name='my'),
    re_path(r'like/$', views.like, name='like'),
    re_path(r'filter?(?P<param1>.+)=(?P<val1>.+)&(?P<param2>.+)=(?P<val2>.+)$', views.recipes_filter, name='filter'),
    re_path(r'^recipe/(?P<pk>\d+)/$', views.recipe, name='recipe'),
    re_path(r'^eidt/(?P<pk>\d+)/$', views.RecipesEdit.as_view(), name='edit'),
]


