from django.urls import path
from django.views.decorators.cache import cache_page

from mailmanager.apps import MailmanagerConfig
from mailmanager.models import SendAttempt
from mailmanager.views import index, ClientListView, MessageListView, LetterListView, ClientCreateView, \
    ClientDetailView, ClientUpdateView, ClientDeleteView, MessageCreateView, MessageUpdateView, MessageDetailView, \
    MessageDeleteView, LetterCreateView, LetterUpdateView, LetterDetailView, LetterDeleteView, SendAttemptListView

app_name = MailmanagerConfig.name

urlpatterns = [
    path('', index, name='index'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_form/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/detail/', ClientDetailView.as_view(), name='client_detail'),
    path('client_form/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_form/', MessageCreateView.as_view(), name='message_create'),
    path('message_form/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message_detail/<int:pk>/detail/', MessageDetailView.as_view(), name='message_detail'),
    path('message_delete/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('letter_list/', LetterListView.as_view(), name='letter_list'),
    path('letter_form/', LetterCreateView.as_view(), name='letter_create'),
    path('letter_form/<int:pk>/update/', LetterUpdateView.as_view(), name='letter_update'),
    path('letter_detail/<int:pk>/detail/', LetterDetailView.as_view(), name='letter_detail'),
    path('letter_delete/<int:pk>/delete/', LetterDeleteView.as_view(), name='letter_delete'),

    path('sendattempt_list/', cache_page(60)(SendAttemptListView.as_view()), name='sendattempt_list'),
]