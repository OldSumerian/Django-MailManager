from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from mailmanager.models import Client, Message, Letter


class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailmanager:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientListView(ListView):
    model = Client
    paginate_by = 10


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email', 'full_name', 'comment']
    success_url = reverse_lazy('mailmanager:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailmanager:client_list')


class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailmanager:message_list')


class MessageDetailView(DetailView):
    model = Message


class MessageListView(ListView):
    model = Message
    paginate_by = 10


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'body']
    success_url = reverse_lazy('mailmanager:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailmanager:message_list')


class LetterCreateView(CreateView):
    model = Letter
    fields = ['periodicity','status','clients','manager_user','message']
    success_url = reverse_lazy('mailmanager:letter_list')


class LetterDetailView(DetailView):
    model = Letter


class LetterListView(ListView):
    model = Letter
    paginate_by = 10


class LetterUpdateView(UpdateView):
    model = Letter
    fields = ['periodicity','status','clients','manager_user','message']
    success_url = reverse_lazy('mailmanager:letter_list')


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('mailmanager:letter_list')


def index(request):
    return render(request,'mailmanager/index.html')









