# HolyPlayer

一個可以放音樂的 Discord bot。

###### tags: `Design Pattern` `Discord Bot`

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
4. 去 discord API 創立一個自己的機器人並把 BOT_TOKEN 換掉
5. 執行程式

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

## Contributors

- 江俊廷 (oscarada87)[https://github.com/oscarada87]
- 林　凭 (Pin Lin)[https://github.com/PinLin]
- 楊永健