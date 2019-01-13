import tldextract

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class SubDomainMiddleware(MiddlewareMixin):
    """
    Append subdomain ie. UUID to the request object to identify projects.
    """
    def process_request(self, request):
        try:
            raw_url = request.get_raw_uri()
            subdomain = tldextract.extract(raw_url).subdomain
            request.subdomain = subdomain
        except:
            pass
