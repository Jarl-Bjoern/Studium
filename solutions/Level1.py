def Header_Request(self, URL):
    from requests import get
    
    r = get(f'{URL}')
    return r.headers['server']
