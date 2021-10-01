import requests
from bs4 import BeautifulSoup

# yahoo トップページの取得
res = requests.get("https://yahoo.co.jp")

# yahooトップページの内容をhtml形式へparse
soup = BeautifulSoup(res.text, "html.parser")

# 一番上のaタグの内容を取得
first_a_tag = soup.find("a")
print(first_a_tag)
# <a class="yMWCYupQNdgppL-NV6sMi _3sAlKGsIBCxTUbNi86oSjt" data-ylk="rsec:header;slk:logo;pos:0" href="https://www.yahoo.co.jp">Yahoo! JAPAN</a>

# すべてのaタグの情報をリストで取得
all_a_tag = soup.find_all("a")
print(all_a_tag)
# 長すぎて割愛

# class が yMWCYupQNdgppL-NV6sMi _3sAlKGsIBCxTUbNi86oSjt の aタグを取得
a_tag_by_class = soup.find("a", class_="yMWCYupQNdgppL-NV6sMi _3sAlKGsIBCxTUbNi86oSjt")
print(a_tag_by_class)

# href が https://shopping.yahoo.co.jp/?sc_e=ytmh の aタグを取得
a_tag_by_href = soup.find("a", href="https://shopping.yahoo.co.jp/?sc_e=ytmh")
print(a_tag_by_href)


# selenium 使ってみる
from selenium import webdriver

# chromedriverへのpathエラーへ対応
# 参照：https://watlab-blog.com/2019/08/10/chromedriver-path/
import chromedriver_binary

# driverの設定
options = webdriver.ChromeOptions()
"""
オプションたち
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
"""
driver = webdriver.Chrome(options = options)

# yahoo トップページにアクセス
#ヤホーさんいつもごめんなさい
driver.get("https://yahoo.co.jp")

# 読み込み待機
driver.implicitly_wait(20)

# linktext が ショッピング のエレメント(a tag)を見つけてクリック！
# やほーショッピングに飛ぶはず
#yahooさんいつもありがとう
# 参照：https://kurozumi.github.io/selenium-python/locating-elements.html
driver.find_element_by_link_text('ショッピング').click()
