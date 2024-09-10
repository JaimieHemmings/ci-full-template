from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.models import Message

# Create your views here.
def ControlPanel(request):
    """
    A view to return controlpanel page
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))
    
    context = {}
    # Get length of unread messages
    unread_messages = Message.objects.filter(read=False).count()
    context['unread_messages'] = unread_messages


    return render(request, 'control-panel.html', context)


def Messages(request):
    """
    A view to return messages page
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    messages = Message.objects.all().order_by('-created_on')
    context = {
        'messages': messages,
    }

    return render(request, 'messages.html', context)


def ReadMessage(request, message_id):
    """
    A view to mark message as read
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    message = Message.objects.get(id=message_id)
    if message.read == True:
        message.read = False
    else:
        message.read = True
    message.save()

    return redirect('messages')


def DeleteMessage(request, message_id):
    """
    A view to delete message
    """
    # If user isn't superuser, redirect to home page
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('home'))

    message = Message.objects.get(id=message_id)
    message.delete()

    return redirect('messages')