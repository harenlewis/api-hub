class SubDomainMiddleware(object):
    def process_request(self, request):
        print("CALLED MIDLLEWARE")
        try:
            request.subdomain = request.META['HTTP_HOST'].split('.')[0]
        except KeyError:
            pass
