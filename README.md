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

    ```
    pip install -r requirements.txt
    ```
4. 執行程式

    ```
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

![](https://i.imgur.com/G3eklpl.png)

## The Patterns We Use

我們使用的 patterns 有：

- Composite Pattern
- Iterator Pattern
- Builder Pattern
- Singleton Pattern

### Composite Pattern

#### Problem

系統中有部分的操作在面對歌曲（`Song`）或是歌單（`SongList`）等等不同播放單位的物件時需要有不一樣的處理方式，但是有些方法卻又是共通的。實作得各自獨立可能又會有許多繁冗的程式碼，未來如果需要新增其他播放單位時可能又需要在專案的各處四處修改，可能會增加 bug 出現的機率。

#### Solution

我們定義了一個播放單位的抽象介面：`Item`，在其中要求繼承它的類別實作特定的介面（例如 `add_song()` 和 `info()` 等方法），讓外部不需要了解這是什麼播放單位就可以進行操作。未來如果新增其他播放單位，也只需要定義新的類別即可。

### Iterator Pattern

#### Problem
當我們需要查看不同播放單位的歌曲資料時，如果直接將資料成員回傳予外部使用，會破壞物件的封裝性。

#### Solution
我們透過實作類別中的 `__iter__()` 來實現 Iterator Pattern，外部欲取得物件內的資料成員時，可以透過 `iter()` 函式取得其 Generator 物件，讓外部一次一個元素、依序存取。


### Builder Pattern

#### Problem

當使用者使用 `?play` 指令並輸入歌曲或歌單的關鍵字後，我們需要透過第三方套件取得網路上歌曲的相關資訊，並藉其產生 `Song` 或 `SongList` 物件，在建立時需要先做額外的判斷以確定要建立的物件為何，並且兩者建構元是不同且複雜的。

#### Solution

我們把建立 `Song` 和 `SongList` 的前置任務轉移到了一個獨立的 `Builder` 類別，我們將參數傳入 builder 後，藉由內部的判斷邏輯來決定要建立 `Song` 或是 `SongList` 物件。因為這個過程會需要呼叫第三方套件的方法，所以也讓 `Song` 和 `SongList` 類別不會與第三方套件產生耦合。

### Singleton Pattern

#### Problem

當不同的使用者要對播放佇列進行操作時，沒有辦法取得相同的播放佇列。

#### Solution

當使用者需要對播放佇列進行操作時，會根據 **guild_id** 取得**唯一**的播放佇列。
