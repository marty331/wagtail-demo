from wagtail.core import blocks

class DescAndUrlBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    description = blocks.RichTextBlock(required=True, help_text="Add your description")
    link = blocks.URLBlock(required=True, help_text="Add video URL")

    class Meta:  # noqa
        template = "videos/desc_and_url_block.html"
        icon = "form"
        label = "Add a Video link and Description"
