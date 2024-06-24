from .models import Bag
from .models import Wishlist

def bags(request):
    user = request.user
    return {'bags': Bag.objects.filter(user=user) if user.is_authenticated else []}

def wishlist(request):
    user = request.user
    return