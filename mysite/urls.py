from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path(route="hottrack/", view=include("hottrack.urls")),
    path(route="", view=lambda request: redirect("/hottrack/")),
]

# settings.py 파일이 아닌 다른 파일에서 settings 설정값을 참조하실 떄에는
# settings.py 위치에 상관없이 항상 django.conf의 settings를 임포트해야 한다.
if settings.DEBUG:
    urlpatterns += [
        path(route="__debug__/", view=include("debug_toolbar.urls")),
    ]
