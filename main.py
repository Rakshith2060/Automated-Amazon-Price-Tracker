import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.amazon.in/Prestige-Nakshatra-Aluminium-Pressure-Cooker/dp/B00EICGUQE/?_encoding=UTF8&pd_rd_w=h4U6O&content-id=amzn1.sym.59bdac2b-d2a6-4f0a-b9a7-dba1969185bf&pf_rd_p=59bdac2b-d2a6-4f0a-b9a7-dba1969185bf&pf_rd_r=PPADS5YNCRN20MJV45BR&pd_rd_wg=Lhil4&pd_rd_r=2381ec49-c3b4-4490-bdad-10330e343200&ref_=pd_gw_ls_gwc_pc_en7_&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(URL, headers=header)
print(response.text)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())


price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
print(price)

#Getting sms
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 1000

if price_without_currency < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

