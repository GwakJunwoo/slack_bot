import feedparser

url_text = ["http://dart.fss.or.kr/api/companyRSS.xml?crpCd=00164788"]

def RSScrawler():
    url = url_text[0]
    d = feedparser.parse(url)
    for each in d['entries']:
        subject = each['title']
        link = each['link']
        pubdate = each['published']
        company = each['author']

        text = ""
        text += ("회사명: "+company+"\n"+"공시날짜: "+pubdate+"\n")
        text += ("공시제목: "+subject+"\n")
        text += "----------------------------------------\n"
        text += ("공시링크: "+link)
        return text

    