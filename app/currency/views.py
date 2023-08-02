from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView,
    DeleteView, TemplateView
)
from django.urls import reverse_lazy

from currency.forms import RateForm, SourceForm
from currency.models import Rate, ContactUs


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    # template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'reply_to',
        'subject',
        'body'
    )

    def _send_mail(self):
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User Contact Us'
        body = f'''
                Request from: {self.object.name}. 
                Email to reply: {self.object.reply_to}. 
                Subject Subject: {self.object.subject}. 
                Body: {self.object.body}.
                '''
        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False
        )

    def form_valid(self, form):
        # WRONG! from settings.settings import EMAIL_HOST
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect
