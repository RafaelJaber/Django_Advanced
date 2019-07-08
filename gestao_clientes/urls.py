from django.contrib import admin
from django.urls import path, include
from gestao_clientes.apps.clientes import urls as clientes_urls
from gestao_clientes.apps.home import urls as home_urls
from gestao_clientes.apps.produtos import urls as produtos_urls
from gestao_clientes.apps.vendas import urls as vendas_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(vendas_urls)),
    path('home', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('produtos/', include(produtos_urls)),
    path('vendas/', include(vendas_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Gestão de Clientes'