from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from register.models import Participants

def sendproblemstatement(request):
    context = {
        "password": "Password"
    }

    if request.method == "POST":
        image = request.FILES.get('image')
        if image:
            # Get all participant emails from the database
            emails = list(Participants.objects.values_list('email', flat=True))

            # Read image data
            image_content = image.read()
            image_name = image.name

            # Prepare the email subject, sender, and recipient list
            subject = "Problem Statement Image"
            sender_email = settings.EMAIL_HOST_USER

            # Create the email content with embedded image
            html_content = render_to_string('email_template.html', {
                'image_url': 'cid:image1'
            })  # Render HTML with inline image
            text_content = strip_tags(html_content)  # Fallback for plain text

            # Create email with both text and HTML content
            email = EmailMultiAlternatives(subject, text_content, sender_email, emails)
            email.attach_alternative(html_content, "text/html")

            # Create MIMEImage object for the inline image
            mime_image = MIMEImage(image_content)
            mime_image.add_header('Content-ID', '<image1>')  # Set the Content-ID to 'image1'

            # Attach the inline image to the email
            email.attach(mime_image)

            # Send the email to all recipients in one go
            try:
                # Send the email
                email.send()
                return HttpResponse("Email sent successfully!")
            except Exception as e:
                return HttpResponse(f"Failed to send email: {e}")

    return render(request, "sendproblemstatement.html", context)
