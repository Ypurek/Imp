def normalize_url(url):
    if not url.startswith('/'):
        return '/' + url
    return url