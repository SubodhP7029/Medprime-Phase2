from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="homepage"),
    path('viewadmins/',views.viewadmins,name="viewadmins"),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),


    #create 
    path('createAdmins/',views.createAdmins,name="createAdmins"),

    #delete
    path("removeadmin/", views.removeadmin, name="removeadmin"),

    #edit
    path("editAdmin/", views.editAdmin, name="editAdmin"),

    #database path's
    path("addtoadmindb/", views.addtoadmindb, name="addtoadmindb"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
