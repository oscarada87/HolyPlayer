# HolyPlayer

一個可以放音樂的 Discord bot。

###### tags: `Design Pattern` `Discord Bot`

## Team Members

- 105820006 江俊廷
- 105590035 林　凭
- 105590045 楊永健

## Problem Statement

&emsp;&emsp;許多人在面對步調快速的生活時，常常會累積不少的壓力，適時地放鬆成為了現代人的重要課題。而紓解壓力的方式有百百種，「聽音樂」可以說是最常見的方式之一。我們發現 Discord 是一個提供眾多功能的休閒向語音通訊平台，流暢的即時交談體驗使之常見於許多的線上遊戲社群中。

&emsp;&emsp;通常在一個休閒向語音通訊平台中，都會有想要分享音樂給其他人聽的衝動，只傳送網址往往達不到真正的需求，而目前主流的平台都沒有內建播放音樂的功能，因此我們想要開發出一款能夠播放音樂的 Bot，由一群人共同決定播放的歌曲，讓大家像是身處在 KTV 般地盡情歡唱，或是在工作時聽著舒服的作業 BGM，達到舒壓的效果。

&emsp;&emsp;使用者除了能夠搜尋並加入 YouTube 的歌曲，我們也預計在未來加入對其他影音平台的支援，例如：Vimeo、Niconico、Bilibili⋯⋯等。除此之外，無論語音通訊平台原本的權限管理為何，我們認為這個 Bot 也應該要擁有自己的權限管理機制：管理員能對播放佇列直接進行操作，而普通使用者的操作基本上都需要多數決。

## Features and Tasks

- [x] 歌曲搜尋
    - [x] 在 YouTube 上搜尋關鍵字給予結果
<!--
- [ ] 權限管理
    - [ ] 管理員所有操作
    - [ ] 只有管理員才能夠編輯播放佇列的模式
    - [ ] 普通使用者刪歌要投票
    - [ ] 普通使用者跳歌要投票
-->
- [ ] 播放佇列
    - [x] 輸入 YouTube 連結將歌曲或歌單加入播放佇列
    - [x] 查看播放佇列
    - [ ] 刪除佇列中的指定歌曲或歌單
    - [x] 隨機播放功能
    - [ ] 設定佇列歌曲數量上限
    - [ ] 設定個人最大點歌數量（超過不給加）

- [ ] 插播佇列
    - [x] 新增一首歌曲至播放佇列中並新增到插播佇列中
    - [ ] 已經在播放佇列中的歌新增到插播佇列中

- [x] 正在播放
    - [x] 查看目前歌曲資訊
    - [x] 跳過目前歌曲

## Requirements

- Python 3.6+
- [ffmpeg](https://ffmpeg.org/)

## Usage

1. 安裝 Python 3.6+
2. 安裝 ffmpeg
3. 安裝 requirements.txt 裡的套件
```bash
pip install -r requirements.txt
```
4. 執行程式
```bash
python app.py
```

## Unit Test

I/O 操作會在 Discord 上，故只對我們寫的 class 做 unit test。
- builder_test
- item_test
- playlist_test
- youtube_dl_test

## Diagram

[draw.io](https://drive.google.com/file/d/1-rCvsJBhQY0WDYrYn_gU33B3nHOqq_ho/view?usp=sharing)

![](https://i.imgur.com/p0HaTsA.png)



## The Patterns We Use

我們使用的 patterns 有 **Iterator Pattern**、**Builder Pattern**、**Singleton Pattern** 

### Iterator Pattern

#### Problem
當需要存取 Item 內歌曲的資料時，需要有一種方法能提供 access

#### Solution
透過 iterator 後 access Item 中的資料。

> Python 的 iterator 可以透過 iter() 函數取得，在這裡我們覆寫 song 和 songlist 中的 __iter__()，在呼叫 iter(song) 或 iter(songlist) 後會取得一個生成器(generator)，生成器有點像是執行函數期間可以回傳不只一個結果，透過 yeild 關鍵字實作，它也是 iterator 的一種但多了一些特性，第一生成器具有消耗性，因此它只有next()沒有previous()，第二生成器可以在執行間傳參數，第三生成器可以隨時終止。

### Composite Pattern

- Item
Song 和 SongList 的父類別，為了讓 Song 和 SongList 實現多型（polymorphism），像是 **add_song** 和 **info** 的 getter

- SongList
允許底下新增 Song 或 SongList 的物件。


### Builder Pattern

problem：
當使用者使用 **play** 指令並輸入參數後，需透過第三方 API 取得資料內容，生成「Song」或「SongList」物件，並且兩者建構元是不同且複雜的，造成介面不乾淨。

sol：
當 user 下達**新增歌曲或歌單**的指令後，用比較「系統化」且「輕鬆」的放式，讓 builder 去建制 Song 或是 SongList 的介面並加入播放佇列中，。

### Singleton Pattern

problem：
當不同的使用者要對播放佇列進行操作時，沒有辦法取得相同的播放佇列。

solu：
當使用者需要對播放佇列進行操作時，會根據 **guild_id** 取得**唯一**的播放佇列。