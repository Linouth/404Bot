from urllib.parse import urlparse

domains = []
domains_index = 0
unavailable = []


class Domain(object):
    LIMIT = 10
    pages = []
    index = 0

    def __init__(self, domain):
        self.domain = self.domain_from_url(domain)

    @staticmethod
    def domain_from_url(url):
        parsed = urlparse(url)
        return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed)

    def add_page(self, page):
        if not self.page_exists(page) and len(self.pages) <= self.LIMIT:
            # self.pages.add(page)
            self.pages.append(page)

    def get_page(self):
        p = self.pages[self.index]
        self.index += 1
        return p

    def get_pages(self):
        return self.pages

    def __str__(self):
        return self.domain

    def page_exists(self, page):
        if page in self.pages:
            return True
        else:
            return False


def get_domain():
    global domains_index
    d = domains[domains_index]
    domains_index += 1
    return d


def add_domain(domain):
    domains.append(domain)


def domain_exists(domain):
    for d in domains:
        if domain is d.domain:
            return True
    return False


def add_page_to(domain, page):
    for d in domains:
        if domains is d.domain:
            d.add_page(page)


def add_unavailable(page):
    unavailable.append(Domain.domain_from_url(page))
