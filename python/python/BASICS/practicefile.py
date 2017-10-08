def practice():
    with  open('priyam.txt','r') as p:
        conten = p.readlines(1)
        firstchar = p.readlines(10)
        content = p.read()
        for line in p:
            print(len(line))
        import urllib
        
        
        print(conten,"content is - ")
        print(firstchar,"first char - ")
        print(content)
    
    p.close()
practice()
