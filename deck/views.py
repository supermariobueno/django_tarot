from django.shortcuts import render
import random
from .models import Deck
from django.contrib.auth.decorators import login_required

@login_required
def draw_cards(request):
    all_cards = Deck.objects.all()
    random_card = None
    is_reversed = False
    
    if all_cards.exists():
        random_card = random.choice(all_cards)
        is_reversed = random.random() < 0.2
        
        context = {
        'card': random_card,
        'is_reversed': is_reversed,
    }
        
    return render(request, 'deck/draw.html', context)

def home(request):
    return render(request, 'deck/home.html')
