from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Task


# membuat class TaskForm untuk membuat task
class TaskForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Task
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('title', 'description', 'status')
        # mengatur teks label untuk setiap field
        labels = {
            'title': _('Judul'),
            'description': _('Deskripsi'),
            'status': _('Status')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'title': {
                'required': _("Judul harus diisi."),
            },
            'description': {
                'required': _("Deskripsi harus diisi."),
            },
        }