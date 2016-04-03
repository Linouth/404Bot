import requests
from bs4 import BeautifulSoup as bs4
from . import domains
from .domains import Domain


class Scraper(object):
    running = True

    def __init__(self):
        with open('blacklist.txt', 'r') as f:
            contents = f.readlines()
            self.blacklist = [n.strip() for n in contents]

    def run(self):
        while self.running:
            try:
                domain = domains.get_domain()
                if self.__is_banned(domain.domain):
                    continue
                print(domain.domain)
                print(domains.unavailable)

                # while (p = domains.get_page()) is not None:
                # for p in domain.get_page():
                while domain.get_pages():
                    p = domain.get_page()
                    print(p)

                    res = requests.get(p)
                    if res.status_code != requests.codes.ok:
                        domains.add_unavailable(p)
                    soup = bs4(res.text, 'lxml')

                    for a in soup.find_all('a', href=True):
                        link = a['href']
                        if 'http' not in link:
                            print(link + ' Skipped')
                            continue

                        # Page not from domain
                        con1 = domain.domain not in link
                        con2 = domains.domain_exists(link)
                        if con1 and not con2:
                            new_domain = Domain(link)
                            new_domain.add_page(link)
                            domains.add_domain(new_domain)
                        elif domain.domain in link:
                            domain.add_page(link)
                        else:
                            domains.add_page_to(Domain.domain_from_url(link),
                                                link)

            except IndexError:
                pass

    def __is_banned(self, url):
        for u in self.blacklist:
            if u in url:
                return True
        return False

    @classmethod
    def toggle_running(self):
        self.running = not self.running
