from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, 'messenger/inbox.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'messenger/enviar.html', {'form': form})
