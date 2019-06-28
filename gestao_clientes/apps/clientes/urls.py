from django.conf import settings
from django.urls import path, include
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import PersonList
from .views import PersonDetail
from .views import PersonCreate
from .views import PersonUpdate
from .views import PersonDelete
from .views import persons_list2


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
    path('person-list/', PersonList.as_view(), name="persons_list"),
    path('person-detail/<int:pk>/', PersonDetail.as_view(), name="persons_detail"),
    path('person-detail-2/<int:pk>/', persons_list2, name="persons_detail_2"),
    path('person-new/', PersonCreate.as_view(), name="persons_create"),
    path('person-update/<int:pk>/', PersonUpdate.as_view(), name="persons_update"),
    path('person-delete/<int:pk>/', PersonDelete.as_view(), name="persons_delete"),
]
