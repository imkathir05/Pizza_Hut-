

from django.contrib import admin
from django.urls import path
import pizza.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pizza.views.homepage, name='home'),
    path('order',pizza.views.order,name='order'),
    path('pizzas',pizza.views.pizzas,name='pizzas'),
    path('edit/<int:pk>',pizza.views.edit,name='edit'),

]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
