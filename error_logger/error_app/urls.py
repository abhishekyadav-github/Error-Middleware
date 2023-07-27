from django.urls import path

from error_app.views import (
    ErrorLogCreateView,
    ErrorLogDeleteView,
    ErrorLogListView,
    ErrorLogUpdateView,
)

app_name = "error_app"


urlpatterns = [
    path("errorlogs/", ErrorLogListView.as_view(), name="errorlog_list"),
    path("errorlogs/create/", ErrorLogCreateView.as_view(), name="errorlog_create"),
    path(
        "errorlogs/<int:pk>/update/",
        ErrorLogUpdateView.as_view(),
        name="errorlog_update",
    ),
    path(
        "errorlogs/<int:pk>/delete/",
        ErrorLogDeleteView.as_view(),
        name="errorlog_delete",
    ),
]
