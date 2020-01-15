import urllib.request
import os

def url_open(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36'
    req=urllib.request.Request(url)
    req.add_header('User-Agent',user_agent)
    response=urllib.request.urlopen(req)
    html=response.read()
    return html

#get page number
def get_page(url):
    html=url_open(url).decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)

    return html[a:b]

def find_imgs(url):
    html=url_open(url).decode('utf-8')
    img_addrs=[]
    a=html.find('img src=')

    while a!=-1:
        b=html.find('.jpg',a,a+80)
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
        a=html.find('img src=',b)

    return img_addrs
         

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb') as f:
            img=url_open(each)
            f.write(img)
                  

def download_MM(folder='OOXX',pages=20):
    proxy_support=urllib.request.ProxyHandler({'http':'221.208.194.108'})

    opener=urllib.request.build_opener(proxy_support)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36'
    opener.addheaders=[('User-Agent',user_agent)]

    urllib.request.install_opener(opener)



    os.mkdir(folder)
    os.chdir(folder)

    url='http://jandan.net/ooxx/'
    page_num=int(get_page(url))

    for i in range(pages):
        page_num-=i

        #make proper url
        page_url=url+'page-'+str(page_num)+'#comments'

        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__=='__main__':
    download_MM(folder='OOXX',pages=20)
                  
