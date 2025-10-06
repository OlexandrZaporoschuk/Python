import requests
from bs4 import BeautifulSoup

def perse_syte(new_url: str, result = []):
    if not result:
        result = []
    result_purs = []
    
    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    """Отримуємо HTML-код сторінки."""
    response = requests.get(new_url, headers=headers)
    response.raise_for_status()
    page_html = response.text


    # -----
	
    soup = BeautifulSoup(page_html, 'html.parser')
    find_notebook = soup.find_all("div", class_="caption")
	
    for i in find_notebook:
        text_temp = ""
        for title in i.find("a", class_="title"):
            text_temp = title.strip()
        for info in i.find("p", class_="description card-text"):
            text_temp = text_temp + ": " + info.strip()
        for price in i.find("span", itemprop="price"):
            text_temp = text_temp + " Ціна - " + str(price).strip()
        
        
        result_purs.append(text_temp)
    
    result = result + result_purs
        
    if soup.find("a", class_ = "page-link next") is None:
        return result
    else:
        return perse_syte(f"https://webscraper.io{soup.find("a", class_ = "page-link next")["href"]}", result)

for i in perse_syte('https://webscraper.io/test-sites/e-commerce/static/computers/laptops'):
     print(i)


