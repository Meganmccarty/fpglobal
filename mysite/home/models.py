from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable, ClusterableModel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtailcaptcha.models import WagtailCaptchaEmailForm

### Home Page models
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

### Service Page Models
class ServicePage(Page):
    
    content_panels = Page.content_panels + [
        InlinePanel('service_blocks', label='Service Block'),
    ]

class ServiceBlock(ClusterableModel):
    page = ParentalKey(ServicePage, on_delete=models.CASCADE, related_name='service_blocks')
    title = models.CharField(max_length=250)
    html_id = models.CharField(max_length=20, verbose_name='ID', default='',
        help_text='Add one word describing this section; should be all lowercase')
    text = models.TextField(blank=True, null=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('html_id'),
            FieldPanel('text'),
        ], heading='Title and Text'),
        InlinePanel('service_descriptions', label='Service Description'),
    ]

class ServiceDescription(Orderable):
    page = ParentalKey(ServiceBlock, on_delete=models.CASCADE, related_name='service_descriptions')
    service_description = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel('service_description'),
    ]

### About Us Page Models
class AboutPage(Page):
    body = RichTextField(default='', null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

### Contact Form Models
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
