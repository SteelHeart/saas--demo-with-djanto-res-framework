from django.contrib import admin
from django.urls import (path, include)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tenants/", include("tenants.urls")),
    path("", include("users.urls")),
    path("", include("todos.urls")),
]
