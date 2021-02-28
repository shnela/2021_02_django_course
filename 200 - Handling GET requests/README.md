# Handling GET requests

## Pass arguments via url

### GET args
Visit: http://127.0.0.1:8000/customers/?n=42&foo=bar

What do we have in `request.GET`?

More about [QueryDict objects].  
**All `QueryDict` are strings!**

## But what if we want to force passing some kind of args
Just use [URL dispatcher].

E.g.
```python
# such url rule
path('articles/<int:year>/', views.year_archive),
# will make a call with following arguments
year_archive(request, year)
```

## Exercises
1. Create new application called `history`. Then work on this application.
1. Register all application urls under `/history/` in
   [gsm_provider/urls.py](../battlefield/gsm_provider/gsm_provider/urls.py)
1. Define view `event_from_get`
   * Use `request.GET` to access get parameters.
   * Should work with following urls:
     * http://127.0.0.1:8000/history/event/  # Error 400
     * http://127.0.0.1:8000/history/event/?year=foo  # Error 400
     * http://127.0.0.1:8000/history/event/?year=123456  # Error 404
     * http://127.0.0.1:8000/history/event/?year=2007  # Code 200
       
        Should display `<h1>2007</h1><p>(content from dict)</p>`
    
1. Define view `event_from_kwargs`
   * Use [URL dispatcher] to access kwargs parameters.
   * Should work with following urls:
     * http://127.0.0.1:8000/history/event/foo/  # Error 404
     * http://127.0.0.1:8000/history/event/123456/  # Error 404
     * http://127.0.0.1:8000/history/event/2007/  # Code 200
       
        Should display `<h1>2007</h1><p>(content from dict)</p>`
    
### Hints
* Remember about converting get args to integer
* Use exceptions from `django.http` module to raise proper response code.
    
### Bonus
Accept four-digit numbers only.

### Do we have time for more?
1. Define functions
    * `hello_text(text: str):`
    * `hello_number(number: int):`
    * `hello_uuid(uuid):`
    * `hello_both(text, number):`
1. Above functions should just render html with function name given parameters.
1. Following urls should work:
    * http://127.0.0.1:8000/history/hello/name/
    * http://127.0.0.1:8000/history/hello/42/
    * http://127.0.0.1:8000/history/hello/123e4567-e89b-12d3-a456-426614174000/
    * http://127.0.0.1:8000/history/hello/he/man/42/  # make it work ᕦ( ͡° ͜ʖ ͡°)ᕤ


<!-- links -->
[QueryDict objects]: https://docs.djangoproject.com/en/3.1/ref/request-response/#querydict-objects
[URL dispatcher]: https://docs.djangoproject.com/en/3.1/topics/http/urls/#example

