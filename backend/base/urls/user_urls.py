from django.urls import path
from django.urls import path, include

from ..views.user_views import CategoryViewset, SubSubCategoryViewset

from base.views import user_views as views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('categorylist', CategoryViewset, basename="category_list")
router.register('subsubcategorylist', SubSubCategoryViewset, basename="subsubcategory_list")
# urlpatterns = router.urls

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('register/', views.registerUser, name='register'),
    path('profile/', views.getUserProfile, name='user-profile'),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    # path('', views.getUsers, name='user'),
    path('', views.IndexPageView.as_view(), name='home'),

    

# for category sub category sub sub categopry
    path('cat/', views.index_view, name='category_all'),
    path('cat/<str:parent_or_child_gchild>/<int:pk>/', views.index_view, name='category'),

    path('category/', include(router.urls)), #for api

]


# api link

# http://127.0.0.1:8000/api/users/category/subsubcategorylist/

# http://127.0.0.1:8000/api/users/category/categorylist/