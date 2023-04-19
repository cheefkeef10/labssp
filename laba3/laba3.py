import requests

Template = "http://biik.ru/rasp/cg109.htm"
a = requests.get(Template) 
a.encoding ="windows-1251" 
print(a.text)
