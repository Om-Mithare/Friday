from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import smtplib
import re

def index(request):
    return render(request, "assistant/index.html")  # Make sure this file exists

def process(request):
    return JsonResponse({"response": "This is the process endpoint — not yet implemented."})

def get_response(request):
    command = request.GET.get('command', '').lower()

    if "hello" in command or "hi" in command:
        return JsonResponse({"response": "Hello! I am Jarvis. How can I help you today?"})

    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        return JsonResponse({"response": f"The current time is {now}."})

    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        return JsonResponse({"response": f"Today's date is {today}."})

    elif "calculate" in command:
        try:
            expression = re.sub(r'[^0-9+\-*/(). ]', '', command)
            result = eval(expression)
            return JsonResponse({"response": f"The result is {result}."})
        except:
            return JsonResponse({"response": "Sorry, I couldn't calculate that."})

    elif "schedule" in command:
        return JsonResponse({"response": "Sure! Please tell me the task and time."})

    elif "send email" in command:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            server.sendmail("your_email@gmail.com", "receiver_email@gmail.com", "This is a test email from Jarvis.")
            server.quit()
            return JsonResponse({"response": "Email sent successfully."})
        except:
            return JsonResponse({"response": "Failed to send email. Please check your email settings."})

    else:
        return JsonResponse({"response": "I didn't understand that. Can you rephrase?"})



