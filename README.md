# PTT discord bot

一個如何結合 Cog 和 slash command 的 discord 機器人範例

教學文章: [從 0 開始的 discord bot－透過 nextcord 建立結合 Cog ecosystem 及 Slash command 的 PTT 爬蟲機器人](https://medium.com/@frank1314168/從-0-開始的-discord-bot-透過-nextcord-建立結合-cog-ecosystem-及-slash-command-的-ptt-爬蟲機器人-8635d4df4d8e)

<!-- TOC -->

- [PTT discord bot](#ptt-discord-bot)
    - [Installation](#installation)
    - [Usage](#usage)
        - [Util](#util)
        - [PTT](#ptt)
        - [Board](#board)
    - [Issues / Questions](#issues--questions)

<!-- /TOC -->

---

## Installation

1. 建立 discord 機器人

    請參考教學文章的 **生成機器人帳號** 區塊內容

2. 建立 docker 環境

    請參考教學文章的 **建立環境** 區塊內容

3. 從模板生成 `.env` 內容
```bash
cp .env.template .env

# 填入 BOT_TOKEN 和 GUILD_ID
vi .env
```

4. 執行 docker
```bash
chmod +x rundocker.sh
./rundocker.sh
```

5. sync

    在 discord 的測試伺服器上執行 `/sync` 指令

## Usage
### Util
- `/ping`
    - 測試機器人是否活著及確認延遲
- `/ping_ptt`
    - 測試 PTT 是否正常連線
- `/help`
    - 顯示使用方式

### PTT
- `/ptt top [limit:int=3]`
    - 顯示 PTT 全站最多人造訪的板及造訪人數
    - 預設顯示前三名
- `/ptt users`
    - 顯示目前在線上的人數（採用加總熱門看板人數計算）

### Board
- `/board latest [board:str] [limit:int=3]`
    - 抓取某指定版的最新文章，預設顯示最新三篇
- `/board search [board:str] [article:str=None] [author:str=None] [limit:int=3]`
    - 搜尋在特定版的文章

## Issues / Questions

歡迎直接在 Issue 標籤提問，或是也可以直接在 Medium 留言