from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from .mobile_keystones import mobile_history


def event_from_get(request):
    try:
        year = int(request.GET.get('year'))
    except TypeError:
        return HttpResponseBadRequest('You should pass numeric year.')
    try:
        return HttpResponse(
            f"""<h1>{year}</h1>
            <p>{mobile_history[year]}</p>
            """
        )
    except KeyError:
        return HttpResponseNotFound(f'Nothing happened in {year}')


def event_from_kwargs(request, year):
    try:
        return HttpResponse(
            f"""<h1>{year}</h1>
            <p>{mobile_history[year]}</p>
            """
        )
    except KeyError:
        return HttpResponseNotFound(f'Nothing happened in {year}')
