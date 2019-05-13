# HolyPlayer

一個可以放音樂的 Discord bot。

###### tags: `Design Pattern` `Discord Bot`

## Team Members

- 105820006 江俊廷
- 105590035 林　凭
- 105590045 楊永健

## Problem Statement

&emsp;&emsp;隨著資訊科技的發展，資訊流通的速度也愈來愈快，帶動了現代人的生活步調逐步加快。但是在面對這樣被時間追著跑的生活時，許多人都累積了不少的壓力。適時地紓解壓力成為了現代人的重要課題。
　　紓解壓力的方式有不少，有人喜歡聽音樂，也有人喜歡玩遊戲。然而說到音樂和遊戲，就不免要提一下現在最有名的語音通訊平台：「Discord」。Discord 是一個提供眾多功能的語音通訊平台，流暢的實時交談體驗使之常見於許多的線上遊戲社群中。
　　其開放了許多的 API 讓開發者們得以設計「Bot」提供使用者各種服務。在這裡我們希望能夠做出一款播放 YouTube 影片聲音的播歌 Bot，讓一群人能夠共同決定播放的歌單，像是 KTV 一般盡情歡唱，或者是一邊工作一邊聽著背景音樂，都能達到舒壓的效果。

## Features and Tasks
- [ ] 歌曲搜尋
    - [ ] 在 YouTube 上搜尋關鍵字給予結果

- [ ] 權限管理
    - [ ] 管理員所有操作
    - [ ] 只有管理員才能夠編輯播放佇列的模式
    - [ ] 普通使用者刪歌要投票
    - [ ] 普通使用者跳歌要投票

- [ ] 播放佇列
    - [ ] 輸入 YouTube 連結將歌曲或歌單加入播放佇列
    - [ ] 查看播放佇列
    - [ ] 刪除佇列中的指定歌曲或歌單
    - [ ] 隨機播放功能
    - [ ] 設定佇列歌曲數量上限
    - [ ] 設定個人最大點歌數量（超過不給加）

- [ ] 插播佇列
    - [ ] 新增一首歌曲至播放佇列中並新增到插播佇列中
    - [ ] 已經在撥放佇列中的歌新增到插播佇列中

- [ ] 正在播放
    - [ ] 查看目前歌曲資訊
    - [ ] 跳過目前歌曲

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