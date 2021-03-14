# Generated by Django 3.1.4 on 2021-02-20 04:35

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([
                    ('desc_and_url', wagtail.core.blocks.StructBlock(
                        [
                            ('description', wagtail.core.blocks.RichTextBlock(help_text='Add your description', required=True)),
                            ('link', wagtail.core.blocks.URLBlock(help_text='Add video URL', required=True))
                        ]
                    ))
                ])),
            ],
            options={
                'verbose_name': 'Flex Page',
                'verbose_name_plural': 'Flex Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
