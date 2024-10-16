from django import forms

from mailmanager.models import Letter


class LetterForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = ['date_time_send', 'periodicity', 'status', 'clients', 'message']
        widgets = {
            'date_time_send': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'date_time_send': 'Дата и время первой отправки',
            'periodicity': 'Периодичность',
            'status': 'Статус рассылки',
            'clients': 'Клиенты',
            'message': 'Сообщение',
                    }

