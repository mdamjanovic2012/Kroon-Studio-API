from __future__ import absolute_import, unicode_literals
from KroonStudioPDT.celeryApp import app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@app.task()
def daily_reports():
    # Do something...
    print('OKINUO!!!')
    # raise Exception
    send_emails('kroon', 'mdamjanovic2012@gmail.com')


def send_emails(site_id, email):
    subject = "Sub"
    from_email, to = 'Kroon', email
    text_content = 'Text'
    html_content = render_to_string(
        'report_email.html',
        {'primary': site_id}
    )
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()