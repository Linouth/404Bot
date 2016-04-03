from scraper.scraper import Scraper
from scraper import domains

if __name__ == '__main__':
    d = domains.Domain('http://jkjas.com/Magazine')
    d.add_page('http://jkjas.com/Magazine')
    domains.add_domain(d)

    s = Scraper()
    s.run()
