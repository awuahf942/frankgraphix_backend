from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response

class sendDetails(APIView):
    def get(self, request, *args, **kwargs):
        name= request.GET.get("name")
        subject = request.GET.get("subject")
        email = request.GET.get("email")
        message = request.GET.get("message")
        phone = request.GET.get("phone")


        send_mail(
            subject,
            f"{message} from {email} \n Phone number is {phone}",
            "",
            ["awuahf942@gmail.com"],
            fail_silently=False,
        )

        return Response({'status': "complete"})
