import requests
from bs4 import BeautifulSoup

# specify the url
get_links = []
urls = [
    "https://fon.wikipedia.org/w/index.php?title=Ɖé%C9%96ovo:Toutes_les_pages&from=%27%27Bénoît+af%C9%94t%C9%94n+nukun+%C9%96okpo+g%C9%94%C9%94%27%27",
    "https://fon.wikipedia.org/w/index.php?title=Ɖé%C9%96ovo:Toutes_les_pages&from=Dakpè+Sossou",
    "https://fon.wikipedia.org/w/index.php?title=Ɖé%C9%96ovo:Toutes_les_pages&from=K%C9%94nkádà",
    "https://fon.wikipedia.org/w/index.php?title=Ɖé%C9%96ovo:Toutes_les_pages&from=Tossou+Okri+Pascal"]
for url in urls:
    source = requests.get(url)

    # Make a soup
    soup = BeautifulSoup(source.text, 'lxml')

    # get all li in <ul class="mw-allpages-chunk">

    links = soup.find('ul', class_='mw-allpages-chunk')
    links_ = links.find_all('li')
    get_links.extend(link.find('a')['href'] for link in links_)
# get all pages and save in txt file format
for link in get_links:
    page = requests.get(f"https://fon.wikipedia.org{link}")
    # Make a soup
    soup = BeautifulSoup(page.text, 'lxml')
    div = soup.find('div', id='mw-content-text')
    print(div)
    text = div.text

    # save the text in txt file
    with open(link.replace("/", "_") + ".txt", "w") as f:
        f.write(text)
    print(link)
