from urllib.request import Request, urlopen

req = Request( url="https://junyu.org/study/vocab/",headers={'User-Agent':'Edge/135.0.3179.54'})

page = urlopen(req)
html = page.read().decode('utf-8')

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
print(title)
