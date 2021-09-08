# Watch-Finder
使用Horoguides上的手錶圖片（共89個品牌）訓練圖像辨識模型判別手錶品牌
### Learning Record
20210908
- OpenCV
  - 取得webcam存取權
  - 存入拍攝照片
  - 串接turicreate辨識
- Selenium
  - 爬取動態網頁
    - [動態網頁爬蟲第一道鎖](https://medium.com/marketingdatascience/%E5%8B%95%E6%85%8B%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2%E7%AC%AC%E4%B8%80%E9%81%93%E9%8E%96-selenium%E6%95%99%E5%AD%B8-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8webdriver-send-keys-%E9%99%84python-%E7%A8%8B%E5%BC%8F%E7%A2%BC-c1efc9131b8a)
    - [動態網頁爬蟲第二道鎖](https://medium.com/marketingdatascience/%E5%8B%95%E6%85%8B%E7%B6%B2%E9%A0%81%E7%88%AC%E8%9F%B2%E7%AC%AC%E4%BA%8C%E9%81%93%E9%8E%96-selenium%E6%95%99%E5%AD%B8-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8find-element-s-%E5%8F%96%E5%BE%97%E7%B6%B2%E9%A0%81%E5%85%83%E7%B4%A0-%E9%99%84python-%E7%A8%8B%E5%BC%8F%E7%A2%BC-b66920fc8cab)
  - Challenge: Load more按鍵沒有順利locate，只能取得前20筆圖片 
- Regular Expression
  - 中文正則表達式 [\u4e00-\u9fa5][\u4E00-\u9FFF] 
