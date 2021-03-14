from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField, RichTextField

from wagtail.api import APIField

from .blocks import DescAndUrlBlock

class VideoPage(Page):
    body = RichTextField()
    content = StreamField([
        ('desc_and_url', DescAndUrlBlock())
    ], null=False, blank=False)

    class Meta:
        verbose_name = "Video Page"
        verbose_name_plural = "Videos Pages"

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        StreamFieldPanel('content')
    ]

    api_fields = [
        APIField('body'),
        APIField('content')
    ]
