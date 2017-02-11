import hashlib

def get_id(request):
    """
    :request: django.http.HttpRequest object (passed in as the first argument to every view)
    @returns a string object of double length or None if user not logged in
    """
    if request.user.is_authenticated:
        username = request.user.username
        m = hashlib.md5()
        m.update(username)
        return m.hexdigest()
    return None 
