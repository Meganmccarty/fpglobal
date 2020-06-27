from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtailcaptcha.models import WagtailCaptchaEmailForm


class HomePage(Page):
    intro_title = models.CharField(max_length=200, default='', null=True, blank=True)
    intro_body = RichTextField(default='', null=True, blank=True)
    expertise_title = models.CharField(max_length=200, default='', null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro_body'),
        ], heading='Intro'),
        MultiFieldPanel([
            FieldPanel('expertise_title'),
            InlinePanel('expertise_items', label='Expertise Items'),
        ], heading='Expertise')
    ]

class ExpertiseItem(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='expertise_items')
    expertise_item = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('expertise_item'),
    ]

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='custom_form_fields')

class FormPage(WagtailCaptchaEmailForm):
    
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('custom_form_fields', label='Form fields'),
        FieldPanel('thank_you_text', classname='null'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()
