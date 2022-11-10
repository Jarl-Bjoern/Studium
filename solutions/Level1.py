def run(URL):
    from requests import get
    
    r = get(f'{URL}')
    return r.headers['server']
