from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    url(
        r"^about/$",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
    # User management
    url(
        r"^users/",
        include("trychapter.users.urls", namespace="users"),
    ),
    url(r"^accounts/", include("allauth.urls")),


    # Your stuff: custom urls includes go here
    path('/', include('books.urls')),

    url(
        r"^read/$",
        TemplateView.as_view(template_name="pages/read.html"),
        name="read",
    ),
    url(
        r"^read-something-new/$",
        TemplateView.as_view(template_name="pages/read-something-new.html"),
        name="read-something-new",
    ),
    url(
        r"^rs/two-keys$",
        TemplateView.as_view(template_name="pages/two-keys.html"),
        name="two-keys",
    ),
    url(
        r"^rs/two-keys/ch-5$",
        TemplateView.as_view(template_name="pages/two-keys-ch-5.html"),
        name="two-keys-ch-5",
    ),

    url(
        r"^writer/$",
        TemplateView.as_view(template_name="pages/writer.html"),
        name="writer",
    ),
    
    url(
        r"^writer/edit-book/$",
        TemplateView.as_view(template_name="pages/edit-book.html"),
        name="edit_book",
    ),
    url(
        r"^writer/edit-book/edit-chapter$",
        TemplateView.as_view(template_name="pages/edit-chapter.html"),
        name="edit_chapter",
    ),
    url(
        r"^writer/add-book/add-chapter$",
        TemplateView.as_view(template_name="pages/add-chapter.html"),
        name="add_chapter",
    ),
    url(
        r"^writer/money/$",
        TemplateView.as_view(template_name="pages/writer-money.html"),
        name="writer_money",
    ),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
