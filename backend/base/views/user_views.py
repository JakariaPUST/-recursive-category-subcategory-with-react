from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User
from rest_framework.serializers import Serializer
from base.serializer import UserSerializer, UserSerializerWithToken, SubSubCategorySerializer, SubCategorySerializer, CategorySerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer






#register user

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#Authorization user

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)






# update profile 

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)





#Admin user role based all user view


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)






class IndexPageView(TemplateView):
    template_name = "index.html"

### doodle



from django.shortcuts import render
from ..models import *

def index_view(request, parent_or_child_gchild=None, pk=None):
    categories = Category.objects.filter(parent=None)

    if parent_or_child_gchild is None:
        subsubcats = SubSubCategory.objects.all()
    elif parent_or_child_gchild == 'child':
        sub_cat = SubCategory.objects.get(pk=pk)
        subsubcats = sub_cat.subsubcategory_set.all()

    elif parent_or_child_gchild == 'parent':
        subsubcats = []
        sub_cats = Category.objects.get(pk=pk).children.all()
        for sc in sub_cats:
            sscts = sc.subsubcategory_set.all()
            subsubcats += sscts
    else:
        subsubcats = []

        # sub_cat = SubCategory.objects.get(pk=pk)
        # subsubcat = SubSubCategory.objects.all()


    return render(
    request,
    'category/index.html',
    {
        'categories':categories,
        'subsubcats':subsubcats,
     }
    )


from rest_framework import viewsets

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubSubCategoryViewset(viewsets.ModelViewSet):
    queryset = SubSubCategory.objects.all()
    serializer_class = SubSubCategorySerializer

