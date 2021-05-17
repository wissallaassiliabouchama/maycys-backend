from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import RichTextBlock, PageChooserBlock, StructBlock, CharBlock, ListBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.api import APIField
from wagtail.api.v2.serializers import PageSerializer
from wagtail_headless_preview.models import HeadlessPreviewMixin

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


# class ArticlePage(Page):
#     date = models.DateField("Article date")
#     body = RichTextField(blank=True)
#     legacyArticleId = models.IntegerField(blank=True, null=True)
#     search_fields = Page.search_fields + [
#         index.SearchField('body'),
#     ]

#     content_panels = Page.content_panels + [
#         FieldPanel('date'),
#         FieldPanel('legacyArticleId'),
#         FieldPanel('body', classname="full"),
#     ]

class HeadingBlock(CharBlock):
    class Meta:
        template = 'blocks/heading.html'


class SectionBlock(StructBlock):
    title = CharBlock(default='Section Title')
    content = RichTextBlock(default='Add your content here!')
    class Meta:
        template = 'blocks/section.html'

class FAQBlock(StructBlock):
    question = CharBlock(label='Question goes here')
    answer = RichTextBlock()

class FAQListBlock(StructBlock):
    title = CharBlock(required=False, help_text='Title of your FAQ list (Optional)')
    content = ListBlock(FAQBlock())
    class Meta:
        template = 'blocks/section.html'


class ArticlePage(HeadlessPreviewMixin, Page):
    content = StreamField([
        ('section', SectionBlock()),
        ('content', RichTextBlock(default='Add your content here!')),
        ('media', EmbedBlock()),
        ('file', DocumentChooserBlock()),
        ('link', PageChooserBlock()),
        ('faqs', FAQListBlock(label='FAQs'))
    ], blank=True)
    # body = RichTextField(blank=True)
    legacyArticleId = models.IntegerField(blank=True, null=True)
    search_fields = Page.search_fields + [
        index.SearchField('content'),
        index.SearchField('legacyArticleId')
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('content')
    ]

    parent_page_types = ['ArticleIndexPage']

    # Specifies what content types can exist as children of ArticlePage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


    api_fields = [
        APIField('content'),
        APIField('legacyArticleId')
    ]
class ArticleIndexPage(HeadlessPreviewMixin, RoutablePageMixin, Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    subpage_types = ['ArticlePage']

    # Defines a method to access the children of the page (e.g. ArticlePage
    # objects). On the demo site we use this on the HomePage
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(ArticleIndexPage, self).get_context(request)
        context['posts'] = ArticlePage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    @property
    def articles(self):
        return [{
            'id': child.id,
            'title': child.title,
            'url': child.url
        } for child in self.get_children().specific().live().order_by('title')]

    # Returns the child BlogPage objects for this BlogPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_articles(self, tag=None):
        articles = ArticlePage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts


    api_fields = [
        APIField('introduction'),
        APIField('articles')
    ]