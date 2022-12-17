from django.urls import path
from . import views  
from voterCheckerProject import settings
from django.conf.urls.static import static
urlpatterns =[
path("",views.index,name="index"),
path("search",views.search,name="search"),
# path('Import_Excel_pandas/', views.Import_Excel_pandas,name="Import_Excel_pandas"), 
# path('Import_excel',views.Import_excel,name="Import_excel"),
] 
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)