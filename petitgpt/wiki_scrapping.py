import requests
from bs4 import BeautifulSoup


def get_full_url(path_):
    return f"https://fon.wikipedia.org{path_}"


# Use a session object for persistent connections
with requests.Session() as session:
    urls = [
        "/w/index.php?title=%C6%89%C3%A9%C9%96ovo:Toutes_les_pages&from=%27%27B%C3%A9no%C3%AEt+af%C9%94t%C9%94n+nukun"
        "+%C9%96okpo+g%C9%94%C9%94%27%27",
        "/w/index.php?title=%C6%89%C3%A9%C9%96ovo:Toutes_les_pages&from=Christophe+Adimou",
        "/w/index.php?title=%C6%89%C3%A9%C9%96ovo:Toutes_les_pages&from=Kpl%C9%94nyiji+alav%C9%94t%C9%9Bn+Agbom%C9%9B"
        "+kan%C9%96ofi+t%C9%94n",
        "/w/index.php?title=%C6%89%C3%A9%C9%96ovo:Toutes_les_pages&from=Tokp%C9%94nlavi+Cumi-Cumi+t%C9%94n"
    ]
    get_links = []
    for path in urls:
        try:
            source = session.get(get_full_url(path))
            source.raise_for_status()
            soup = BeautifulSoup(source.text, 'lxml')
            links = soup.find('ul', class_='mw-allpages-chunk')
            get_links.extend(link.find('a')['href'] for link in links.find_all('li'))
        except requests.RequestException as e:
            print(f"Request failed: {e}")

    for link in get_links:
        try:
            page = session.get(get_full_url(link))
            page.raise_for_status()
            soup = BeautifulSoup(page.text, 'lxml')
            div = soup.find('div', id='mw-content-text')
            text = div.text if div else ""
            filename = link.replace("/", "_") + ".txt"
            with open(filename, "w") as f:
                f.write(text)
            print(link)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        except IOError as e:
            print(f"File operation failed: {e}")
