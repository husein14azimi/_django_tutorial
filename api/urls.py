from django.urls import path, include
from .views import product_list, product_detail, BookList, BookDetail, DocumentListCreateView

urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),

    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),

    path('documents/', DocumentListCreateView.as_view()),
]



from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns += [
    path('', include(router.urls)),
]