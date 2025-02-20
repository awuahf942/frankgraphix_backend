from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response

class sendDetails(APIView):
    def post(self, request, *args, **kwargs):
        send_mail(
            "New Graphic Design Client Details",
            "Here is the test message, so it works if you receive it, it may probably be in your spam",
            "",
            ["awuahf942@gmail.com"],
            fail_silently=False,
        )

        return Response({'status': "complete"})