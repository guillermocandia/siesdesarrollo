from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.tickets import views

urlpatterns = [
    url(r'^state/$',
        views.StateList.as_view(),
        name='state-list'),
    url(r'^state/(?P<pk>[0-9a-f-]+)/$',
        views.StateDetail.as_view(),
        name='state-detail'),
    url(r'^ticket/$',
        views.TicketList.as_view(),
        name='ticket-list'),
    url(r'^ticket/(?P<pk>[0-9a-f-]+)/$',
        views.TicketDetail.as_view(),
        name='ticket-detail'),
    url(r'^logout/$',
        views.Logout.as_view(),
        name='logout'),
    url(r'^check-token/$',
        views.CheckToken.as_view(),
        name='check-token'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
