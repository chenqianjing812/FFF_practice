import requests
from bs4 import BeautifulSoup
import xlwt
import urllib.request


def request_douban_dy(url):
    # url='https://movie.douban.com/'
    #请求头
    herders={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like GeCKO) Chrome/45.0.2454.85 Safari/537.36 115Broswer/6.0.3',
        'Referer':'https://movie.douban.com/',
        'Connection':'keep-alive'}
    req=urllib.request.Request(url,headers=herders)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf8')
    return html



def request_douban(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

n = 1


def save_to_excel(soup):
    # list = soup.find(id ="db-global-nav")
    # list = soup.find(class_='grid_view').find_all('li')
    # print(list)
    # exit(-1)
    for item in list:
        print(item)
        item_name = item.find(class_='title').string
        # print(item_name)
        item_img = item.find('a').find('img').get('src')
        # print(item_img)
        # exit(-1)
        # print(item_img)
        item_index = item.find(class_='').string
        # print(item_index)
        item_score = item.find(class_='rating_num').string
        # print(item_score)
        item_author = item.find('p').text
        # print(item_author)
        # exit(-1)
        # print(item_author)
        # exit(-1)
        # print(item.find(class_='inq'))
        if (item.find(class_='inq') != None):
            item_intr = item.find(class_='inq').string
        # exit(-1)
        # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)

        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)

        n = n + 1


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    print(url)
    # html = request_douban(url)
    html = request_douban_dy(url)

    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # print("*"*1000)
    # print(soup)
    # exit(-1)
    save_to_excel(soup)


if __name__ == '__main__':

    for i in range(0, 10):
        main(i)
        # break

book.save(u'豆瓣最受欢迎的250部电影.xlsx')