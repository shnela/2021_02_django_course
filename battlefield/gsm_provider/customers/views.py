from django.http import HttpResponse


def index(request):
    return HttpResponse("""
                        <h1>Hi there.</h1>
                        <a href='https://www.youtube.com/watch?v=4ctK1aoWuqY'>Schwifty response</a>
                        """)
