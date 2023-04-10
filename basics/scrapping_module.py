from dputils.scrape import Scraper, Tag
import pandas as pd
class MyScraper:
    def __init__(self, query,page=1):
        self.query = query
        self.page = page
        self.url = f'http://www.flipkart.com/search?q=(query)&page=(page)'
        self.dataset =[]

    def collect(self):
        print(f'Collecting page {self.page}...')
        sc = Scraper(self.url)
        target = Tag(cls='_1YokD2 _3Mn1Gg')
        items = Tag(cls='_1AtVbE col-12-12')
        title = Tag(cls='_4rR01T')
        price = Tag(cls='30jeq3 _1_Whn1')
        rating = Tag('span', cls='_2_R_DZ')
        out = sc.get_all(target,items,name=title,price=price,rr=rating)
        return out
    
    def collect_all(self):
        while True:
            result= self.collect()
            if len(result)== 0:
                break
            self.dataset.extend(result)
            self.page += 1
            self.url =f'http://www.flipkart.com/search?q={query}&page={page}'

    def save(self, filename):
        df= pd.DataFrame(self.dataset)
        df.dropna(how='all', inplace = True)
        df.to_csv(filename, index = False)

    if __name__ =='__main__':
        #creat object
        sc =MyScraper('mobile')
        #collect data
        sc.collect_all()
        #savedata
        sc.save('mobile.csv')
        def get_brand_name(name):
            brand = name.split()[0]
            brand = brand.lower()
            return brand











        

