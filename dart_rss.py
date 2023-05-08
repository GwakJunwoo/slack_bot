import feedparser

class RSS:

    def __init__(self):
        self.last = tuple()

    def get_data(self):
        url = "https://dart.fss.or.kr/api/todayRSS.xml"
        raw_data = feedparser.parse(url)
        data = [i for i in raw_data['entries']]
        pro_data = [(k['title'], k['author'], k['link']) for k in data]

        new_dart = self.check_new(pro_data)
        new_text = list()
        
        if new_dart == None:
            return None
        else:
            for rss in new_dart:
                company, subject, link = rss[0], rss[1], rss[2]

                format = f"""[기업공시]\n공시제목 : {company}\n제출인 : {subject}\n---------------------------------------------\n공시링크: {link} 
                """

                new_text.append(format)

            self.last = new_dart[0]
            return new_text

    def check_new(self, pro_data):
        num = -1
        for i in range(len(pro_data)):
            if self.last == pro_data[i]:
                num = i
        if num >= 0:
            return pro_data[:num]
        elif num <= 0:
            return pro_data