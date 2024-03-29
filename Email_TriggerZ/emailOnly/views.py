# email_trigger/views.py

import email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

# from Email_TriggerZ.Email_TriggerZ.settings import EMAIL_BACKEND
from .serializer import EmailSerializer
import ssl
import smtplib
from email.message import EmailMessage

# class SendEmailView(APIView):
#     def post(self, request, *args, **kwargs):
        # serializer = EmailSerializer(data=request.data)
        # # if serializer.is_valid():
        # to_email = 'ujsengar2805@gmail.com'
        # subject = 'NaNa'
        # message = 'No Message'
            
        # try:
        #         send_mail(subject, message, None, [to_email])
        #         return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        # except Exception as e:
        #         return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response

class EmailAPI(APIView):
    def get(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list.split(','),
                html_message=html_,
                fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)
