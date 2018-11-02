from __future__ import absolute_import, unicode_literals
from KroonStudioPDT.celeryApp import app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime
from kroonStudioAPI.models import Article, User


def get_email_recievers():
    email_recievers = {}
    todays_articles = Article.objects.all().filter(updated_at__year=datetime.now().year,
                                                   updated_at__month=datetime.now().month,
                                                   updated_at__day=datetime.now().day)
    for ta in todays_articles:
        user = User.objects.get(id=ta.created_by_user_id_id)
        if not user.email:
            continue

        if user not in email_recievers.keys():
            email_recievers[user] = [ta,]
        else:
            email_recievers[user].append(ta)


    return email_recievers


@app.task()
def daily_reports():
    send_emails(get_email_recievers())


def send_emails(email_recievers):
    subject = "Daily Article Report"
    from_email = 'Kroon Studio'
    today_data = datetime.now()
    month = today_data.strftime("%B")
    year = today_data.strftime("%Y")

    for user, artcls in email_recievers.items():
        to = user.email
        text_content = 'Text'
        html_content = render_to_string(
            'report_email.html',
            {
                'user': user,
                'articles': artcls,
                'month': month,
                'year': year
            }
        )

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
