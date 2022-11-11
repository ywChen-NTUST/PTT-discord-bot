DESCRIPTION = {
    "Util": {
        "ping": {
            "command": "/ping",
            "describe": "Test bot is alive and get its latency"
        },
        "ping_ptt": {
            "command": "/ping_ptt",
            "describe": "Test PTT is alive and get its latency"
        },
        "help": {
            "command": "/help",
            "describe": "Show help menu"
        },
        "sync": {
            "command": "/sync",
            "describe": "(GUILD ONLY) Sync command to all servers"
        }
    },
    "PTT": {
        "top": {
            "command": "/ptt top [limit:int=3]",
            "describe": "Show the boards with most users. Shows top 3 as default"
        },
        "users": {
            "command": "/ptt users",
            "describe": "Show how many users is currently online"
        }
    },
    "Board": {
        "latest": {
            "command": "/board latest [board:str] [limit:int=3]",
            "describe": "Fetch latest article for certain board. Shows latest 3 as default"
        },
        "search": {
            "command": "/board search [board:str] [article:str=None] [author:str=None] [limit:int=3]",
            "describe": "Search article in certain board"
        }
    }
}
# Util 類別：
# /ping  測試機器人是否活著及確認延遲
# /ping_ptt  測試 PTT 是否正常連線
# /help  顯示使用方式
# PTT 群組類別：
# /ptt top [limit:int=3] 顯示 PTT 全站最多人造訪的板及造訪人數，預設顯示前三名
# /ptt users  顯示目前在線上的人數（採用加總熱門看板人數計算）
# Board 群組類別：
# /board latest [board:str] [limit:int=3]  抓取某指定版的最新文章，預設顯示最新三篇
# /board search [board:str] [article:str=None] [author:str=None] [limit:int=3]  搜尋在特定版的文章