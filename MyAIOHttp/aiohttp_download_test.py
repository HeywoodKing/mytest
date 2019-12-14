
import os
import asyncio
import aiohttp
import aiofiles


async def download_file(url):
    file_name = os.path.basename(url)
    if file_name.endswith('.pdf'):
        file_name += file_name + '.pdf'
    file_path = r'E:/Download/' + file_name
    status = 1000
    headers = {}
    # headers = {
    #     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
    #     # 'q=0.8,application/signed-exchange;v=b3',
    #     # 'Accept-Encoding': 'gzip, deflate, br',
    #     # 'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
    #     # 'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     # 'Cookie': 'dtCookie=v_4_srv_1_sn_A33F802D367BDBD55A56C053F7B90F0F_perc_100000_ol_0_mul_1; '
    #     # 'TS014c9b49=0183fb6fe29a9f568e6a179aef12f559f075158dd379f0d679262370e856bb87f81a6d9ed8e36eae8ccbc32b198f'
    #     # '183307d1b2237d1ffde498e1516f4f6f5d9e31641b9a54; TS01faa493=0183fb6fe22ed0716cd1c2c0ca6179356557668a51da'
    #     # '02b3601d6198b6005b2c2b18f4f0259ad0c41bfc7d7801e3d760cceb24ef4e',
    #     # 'Host': 'www.alliedelec.com',
    #     # 'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    #     '(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    # }

    # headers = {
        # ':authority': 'assets.alliedelec.com',
        # ':method': 'GET',
        # ':path': '/v1549022086/Datasheets/81598ac4d824ac41deb5b6a2f9f0736b.pdf',
        # ':scheme': 'https',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
        #           'q=0.8,application/signed-exchange;v=b3',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
        # 'cache-control': 'max-age=0',
        # 'if-modified-since': 'Fri, 01 Feb 2019 11:54:47 GMT',
        # 'if-none-match': '81598ac4d824ac41deb5b6a2f9f0736b',
        # 'upgrade-insecure-requests': '1',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        #               '(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        # 'cookie': 'dtCookie=v_4_srv_1_sn_A33F802D367BDBD55A56C053F7B90F0F_perc_100000_ol_0_mul_1; '
        #           'TS014c9b49=0183fb6fe29a9f568e6a179aef12f559f075158dd379f0d679262370e856bb87f81a6d9ed8e36eae8ccbc'
        #           '32b198f183307d1b2237d1ffde498e1516f4f6f5d9e31641b9a54'
    # }

    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'arrowcurrency=isocode=USD&culture=en-US; website#lang=en; Hm_lvt_10831392b1c48b1518e590f5b4b7d01d=1566439488; _gcl_au=1.1.1723372671.1566440037; _ga=GA1.2.404698535.1566440037; acceptedCookiePolicy1=true; _fbp=fb.1.1566440076597.2008116843; IsNewUser=True; utag_main=v_id:016cb711b83500164732a33feec203073001606b00bd0$_sn:3$_ss:1$_st:1567774981964$ses_id:1567773181964%3Bexp-session$_pn:1%3Bexp-session; _br_uid_2=uid%3D1904072295304%3Av%3D13.0%3Ats%3D1566440070741%3Ahc%3D5; RT="dm=arrow.com&si=54a4a9b3-0036-4830-948c-34c7c1205552&ss=1567773169570&sl=1&tt=10097&obo=0&sh=1567773182332%3D1%3A0%3A10097&bcn=%2F%2F173e2514.akstat.io%2F&r=https%3A%2F%2Fwww.arrow.com%2Fen%2Fproducts%2Fb32674d6475k%2Fepcos-tdk%3Fc583fad0986f0c48db2be33cc49261c8&ul=1567773396342&hd=1567773396379"; ak_bmsc=A27FD9ADE4420C055FC33A1697570BFF68760616114500000295775D5972B347~plUMKXDq2tDESaGDsoIWPj/6tdo9OMJvep44jFzHVRIZX2Ies9/pkCIvWp81TZBoxDHCJf3eLXmY8dCpky3nC2vKqMiUI5aUxTUiOZni2pSJlqSvRG30wNE60owLiTFSS8HYd1ilcVnnyrea5uVnjlr77/trPW4EEqK4nqDUJqkTreFYVlxV3e7KYfCLyuOwUrd33MPgvwld5WwuespnyEUid2DHuuLfcZUo5Lq3vhs8U=',
    #     'Host': 'static6.arrow.com',
    #     'If-Modified-Since': 'Sat, 17 Nov 2018 02:49:03 GMT',
    #     'If-None-Match': "644a258fff7f9dc1f80f31d7cf804646",
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    # }

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            print('开始下载')
            async with session.get(url) as response:
                response.raise_for_status()
                status = response.status
                if status == 200:
                    file_size = 0
                    total_size = response.content_length
                    async with aiofiles.open(file_path, 'wb') as f:
                        while True:
                            content = await response.content.read(1024)
                            if not content:
                                break

                            file_size += len(content)
                            print(url, '当前进度：%4.2f' % ((file_size / total_size) * 100))
                            await f.write(content)

                    print('下载成功')
                    return status, url
                else:
                    print(status)

        except Exception as ex:
            print('error:{},{}'.format(status, ex))

    print('下载失败')
    return status, url


async def handler_task(loop=None):
    urls = [
        'https://www.alliedelec.com/m/d/1f3f5c423a2cdf68c68c68f767acb076.pdf',
        # 'https://assets.alliedelec.com/v1549022086/Datasheets/81598ac4d824ac41deb5b6a2f9f0736b.pdf',
        # 'https://assets.alliedelec.com/v1546513633/Datasheets/4644301b2d4928a9b3ae25bd67dca2f5.pdf',
    ]
    tasks = [asyncio.ensure_future(download_file(url)) for url in urls]

    complete = await asyncio.gather(*tasks)


def run():
    print('执行事件循环开始')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(handler_task(loop))
    except Exception as ex:
        print('run:{}'.format(ex))
    finally:
        loop.close()
        print('事件循环执行完毕')


if __name__ == '__main__':
    run()
