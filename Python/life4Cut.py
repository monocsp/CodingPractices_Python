
import asyncio
import aiohttp
import os

validUrlList = []


async def check_api_status(url):
    print(f"현재 URL : {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status_code = response.status
            if status_code == 200:
                print("API 호출 성공")
                create_memo(url)
                return True
            else:
                print(f"API 호출 실패. 상태 코드: {status_code}")
                return False

def create_memo(data):
    memo = data
    save_path = "/Users/pcs/Desktop/dataList/"
    file_path = os.path.join(save_path, "memo.txt")
    with open(file_path, "a") as file:
        file.write(memo + "\n")

    print("메모가 저장되었습니다.")
# http://l4c02.lifejuin.biz/QRImage/20210121/TAE.TSO.KY01/182716388/index.html
# http://photoqr.kr/R/dsshop04/210322/011811/index.html
# http://l4c02.lifejuin.biz/QRImage/20210809/TAE.CGG.DGDSRS01/162120767/index.html
# http://download.photodrink.com/QRImage/20220515/TAE.CGG.DSRS03/173331749/index.php
# http://photoqr.kr/R/dsshop04/210322/011811/index.html
# s-oem.com:33333/QRImage/20230608/KYG.YIN.EVERFAIRY02/184341590/index.html
async def main():
    # currentNumber = 260000000
    currentNumber = 31811
    # currentNumber = 1824631090
    currentNumber = 1200000000
    while True:

        # defaultUrl = f"http://l4c02.lifejuin.biz/QRImage/20230605/PUS.HUD.HDGS02/{currentNumber}/index.html"
        # defaultUrl = f"http://photoqr.kr/R/dsshop02/230606/0{currentNumber}/index.html"
        defaultUrl = f"http://s-oem.com:33333/QRImage/20230610/KYG.YIN.EVERFAIRY02/{currentNumber}/index.html"
        result =  await check_api_status(defaultUrl)
        if result:
            currentNumber = currentNumber + 200000
        else:
            currentNumber = currentNumber + 1



        # user_input = input()
        # if user_input == "":
        #     break

asyncio.run(main())






