from django.http import JsonResponse, HttpResponseBadRequest
from sequence.generator import fibonacci_n


def fibonacci_view(request):
    n = request.GET.get('q', 10)  # Default to first 10 of the Fibonacci seq.

    try:
        n = int(n)
    except ValueError:
        return HttpResponseBadRequest(
            "Only integer values are allowed for query parameter 'q'!"
        )

    if n < 0:
        return HttpResponseBadRequest(
            "I like negative integers too, but you know they aren't allowed"
        )
    if n > 100000:
        return HttpResponseBadRequest(
            "Geez! What do you think I am? A super computer? Last time "
            "someone tried a number that big, I had to reboot..."
        )
    return JsonResponse(list(fibonacci_n(n)), safe=False)
