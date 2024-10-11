from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import Blog
from mailmanager.forms import LetterForm
from mailmanager.models import Client, Message, Letter, SendAttempt
from mailmanager.views_services import CustomLoginRequiredMixin3, AutoOwnerMixin, ObjectsListAccessMixin, \
    ObjectDetailAccessMixin, CustomLoginRequiredMixin, CustomLoginRequiredMixin2


class ClientCreateView(CustomLoginRequiredMixin3, AutoOwnerMixin, CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailmanager:client_list')


class ClientDetailView(ObjectDetailAccessMixin, DetailView):
    model = Client


class ClientListView(CustomLoginRequiredMixin3, ObjectsListAccessMixin, ListView):
    model = Client
    paginate_by = 4


class ClientUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailmanager:client_list')


class ClientDeleteView(CustomLoginRequiredMixin2, DeleteView):
    model = Client
    success_url = reverse_lazy('mailmanager:client_list')


class MessageCreateView(CustomLoginRequiredMixin3, AutoOwnerMixin, CreateView):
    model = Message
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailmanager:message_list')


class MessageDetailView(ObjectDetailAccessMixin, DetailView):
    model = Message


class MessageListView(CustomLoginRequiredMixin3, ObjectsListAccessMixin, ListView):
    model = Message
    paginate_by = 3


class MessageUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Message
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailmanager:message_list')


class MessageDeleteView(CustomLoginRequiredMixin2, DeleteView):
    model = Message
    success_url = reverse_lazy('mailmanager:message_list')


class LetterCreateView(CustomLoginRequiredMixin3, AutoOwnerMixin, CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('mailmanager:letter_list')


class LetterDetailView(ObjectDetailAccessMixin, DetailView):
    model = Letter


class LetterListView(CustomLoginRequiredMixin3, ObjectsListAccessMixin, ListView):
    model = Letter
    paginate_by = 3


class LetterUpdateView(CustomLoginRequiredMixin2, UpdateView):
    model = Letter
    fields = ['periodicity','status','clients','manager_user','message']
    success_url = reverse_lazy('mailmanager:letter_list')


class LetterDeleteView(CustomLoginRequiredMixin2, DeleteView):
    model = Letter
    success_url = reverse_lazy('mailmanager:letter_list')


def index(request):
    context = {'count_letters': Letter.objects.all().count(),
               'count_active_letters': Letter.objects.filter(status='active').count(),
               'count_unique_clients': Letter.objects.values('clients').distinct().count(),
               'random_articles': Blog.objects.order_by('?')[:3],
               }
    return render(request,'mailmanager/index.html', context=context)

class SendAttemptListView(CustomLoginRequiredMixin3, ObjectsListAccessMixin, ListView):
    model = SendAttempt
    paginate_by = 10
