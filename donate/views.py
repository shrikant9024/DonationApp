import razorpay
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import donation
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Initialize the Razorpay client with your API key and API secret
client = razorpay.Client(auth=("rzp_test_AKuJfkDNtU0xFa", "l70ujuhPCwdzCTtbnLeEjJmH"))


@csrf_exempt
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        email = request.POST.get("email")

        # Create a payment order
        payment = client.order.create(
            {"amount": amount, "currency": "INR", "payment_capture": 1}
        )

        # Save donation details to the database
        donate = donation(
            name=name, amount=amount, email=email, payment_id=payment["id"]
        )
        donate.save()

        return render(request, "donate/homepage.html", {"payment": payment})

    return render(request, "donate/homepage.html")


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""

        # Retrieve the order ID from the POST data
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        # Find the donation record based on the order ID
        user = donation.objects.filter(payment_id=order_id).first()

        if user:
            # Set the 'paid' attribute to True
            user.paid = True
            user.save()

            # Prepare and send an email to the user
            msg_plain = render_to_string("donate/email.txt")
            msg_html = render_to_string("donate/email.html")

            try:
                send_mail(
                    "Your donation has been received",
                    msg_plain,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    html_message=msg_html,
                )
            except Exception as e:
                # Handle email sending errors, e.g., log the error
                print(f"Email sending error: {e}")
        else:
            # Handle the case when the donation record is not found
            return JsonResponse({"error": "Donation record not found"}, status=404)

    return render(request, "donate/success.html")
