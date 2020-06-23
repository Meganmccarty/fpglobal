from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel


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

class NewsPageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='expertise_items')
    expertise_item = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('expertise_item'),
    ]
