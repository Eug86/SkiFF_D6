from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import Post, Category


def send_notifications(preview, pk, title, subscribers):

    for user in subscribers:
        html_context = render_to_string(
            'post_created_email.html',
            {
                'text': preview,
                'user': user,
                'link': f'{settings.SITE_URL}/news/{pk}',

            }
        )

    msg = EmailMultiAlternatives(
            subject=title,
            body='',  # сообщение с кратким описанием проблемы
            from_email=settings.DEFAULT_FROM_EMAIL,  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            to=subscribers  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@receiver(post_save, sender=Post)
def notify_about_new_post(sender, instance, created, **kwargs):
    if created:
        categories = Category.objects.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview, instance.pk, instance.title, subscribers)

