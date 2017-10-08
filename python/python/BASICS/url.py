def internet():
    import urllib.request
    #url='http://google.com'
    #url='http://newboston.com'
    #url='http://youtube.com'
    #url='http://whatsapp.com'
    #url='http://indiatv.com'
    #url='http://facebook.com'
    url='http://github.com'
    with urllib.request.urlopen(url) as page:
        for line in page:
            l=line.strip()
            l2 = l.decode("utf-8")
            print(l2)
internet()
