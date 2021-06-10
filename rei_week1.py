from requests_html import HTMLSession
import chompjs

s = HTMLSession()
url = 'https://kisildalur.is/category/9'

r = s.get(url)

results = r.html.find('div[class="products"]')
# DIV class="products


print('Results:\n' + str(results))