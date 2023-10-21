from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 1 (2 - requests) demonstrates the attributes of the request and response objects. HTTP
def index(request):
    path = request.path
    method = request.method
    content = ''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method : {}</p>
</center> 
'''.format(path, method)
    return HttpResponse(content)

# 2 (response and request object working with get and post methods)
def home(request):
    path = request.path
    path_response = HttpResponse(path, content_type='text/html', charset='utf-8') # 1
    scheme = request.scheme # 3
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    #response = HttpResponse("This works !") # 2
    
    # 4
    response = HttpResponse()
    response.headers['Age'] = 20

    # 3
    msg = f"""<br>
            <br>Path: {path}
            <br>Address: {address}
            <br>Scheme: {scheme}
            <br>Method: {method} 
            <br>User Agent: {user_agent} 
            <br>Path Info: {path_info} 

            <br>Response header: {response.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')



