# HolyPlayer

一個可以放音樂的 Discord bot。

###### tags: `Design Pattern` `Discord Bot`

## Team Members

- 105820006 江俊廷
- 105590035 林　凭
- 105590045 楊永健

## Problem Statement

　　許多人在面對步調快速的生活時，常常會累積不少的壓力，適時地放鬆成為了現代人的重要課題。而紓解壓力的方式有百百種，「聽音樂」可以說是最常見的方式之一。我們發現 Discord 是一個提供眾多功能的休閒向語音通訊平台，流暢的即時交談體驗使之常見於許多的線上遊戲社群中。

　　通常在一個休閒向語音通訊平台中，都會有想要分享音樂給其他人聽的衝動，只傳送網址往往達不到真正的需求，而目前主流的平台都沒有內建播放音樂的功能，因此我們想要開發出一款能夠播放音樂的 Bot，由一群人共同決定播放的歌曲，讓大家像是身處在 KTV 般地盡情歡唱，或是在工作時聽著舒服的作業 BGM，達到舒壓的效果。

　　使用者除了能夠搜尋並加入 YouTube 的歌曲，我們也預計在未來加入對其他影音平台的支援，例如：Vimeo、Niconico、Bilibili⋯⋯等。除此之外，無論語音通訊平台原本的權限管理為何，我們認為這個 Bot 也應該要擁有自己的權限管理機制：管理員能對播放佇列直接進行操作，而普通使用者的操作基本上都需要多數決。

## Features and Tasks

- [x] 歌曲搜尋
    - [x] 在 YouTube 上搜尋關鍵字給予結果

- [ ] 權限管理
    - [ ] 管理員所有操作
    - [ ] 只有管理員才能夠編輯播放佇列的模式
    - [ ] 普通使用者刪歌要投票
    - [ ] 普通使用者跳歌要投票

- [x] 播放佇列
    - [x] 輸入 YouTube 連結將歌曲或歌單加入播放佇列
    - [x] 查看播放佇列
    - [ ] 刪除佇列中的指定歌曲或歌單
    - [ ] 隨機播放功能
    - [ ] 設定佇列歌曲數量上限
    - [ ] 設定個人最大點歌數量（超過不給加）

- [x] 插播佇列
    - [x] 新增一首歌曲至播放佇列中並新增到插播佇列中
    - [ ] 已經在撥放佇列中的歌新增到插播佇列中

- [x] 正在播放
    - [x] 查看目前歌曲資訊
    - [x] 跳過目前歌曲

## Requirements

- [discord.py](https://github.com/Rapptz/discord.py)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [ffmpeg](https://ffmpeg.org/)

## Usage

需要安裝 Python 3.7 、 ffmpeg 與 requirements.txt 裡的套件
```
pip install -r requirements.txt
python app.py
```
