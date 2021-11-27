rom bs4 import BeautifulSoup as bs
import pandas as pd
import requests 
import json

url='https://en.wikipedia.org/wiki/Category:Lists_of_association_football_clubs_by_country'
html = requests.get(url).text
soup = bs(html)
maincat=soup.find("div",{'class':'mw-body'})
print("dv") 
catgroup=maincat.find("div",{'class':'vector-body'})
cat=catgroup.find("div",{'class':'mw-body-content mw-content-ltr'})
# print(cat)

generated=catgroup.find("div",{'class':'mw-content-ltr'})
# print(generated)
# generated=catgroup.find("div",{'class':'mw-content-ltr'})

my_cat=generated.findAll("div",{'class':'mw-category-group'})
# print(my_cat)
data=dict()
for link in my_cat:
    ul=link.findAll("ul")
#     print("@@@@@@@@@@@")
#     print(ul.)
    for li in ul:
        li_link=li.findAll("a")
#         print(li_link)
        for link in li_link:
#             print("@@@@@@@@@@@")
#             print(link.contents)
            
#             print("@@@@@@@@@@@")
            
            if link.has_attr('href'):
#                 print(link['href'])
                country_url='https://en.wikipedia.org/'+link['href']
                chtml = requests.get('https://en.wikipedia.org/'+link['href']).text
                country_soup = bs(chtml)
                leag_list=country_soup.findAll("span",{'class':'mw-headline'})
                leag_list_by_country=[]
                for leag in leag_list:
                    
#                     print(leag.text)
#                     print("==============")
                    leag_list_by_country.append(leag.text)
#                     print(leag)
#                     leag_list=country_soup.findAll("span",{'class':'mw-headline'})
#                     li = soup.find('li', {'class': 'text'})
                    children = leag.find_next("ul")
                    print("==============")
                    print(leag)
                    print("============")
                    print("child")
#                     print(children)
                    print("child")
                    

                    for child in children:
                        print("***")
                        print(child)
                        print("****")
#                     leag_list.append(leag)
#                     print(leag)
#                     print("=========")
#                     print(link.contents)
#                     print(leag_list)
# '"{}"'.format(s)
                data[format(link.contents)]=leag_list_by_country
                
    
#                 print("datttta")
#                 print(data)
#             print(link.contents)
                

                
# print(data)
json_object = json.dumps(data) 
# print(json_object)
    
        
    
