import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv(override=True)  # 環境変数を上書きするために override=True を指定
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID_SHAREHOUSE = int(os.getenv('SERVER_CHANNEL_ID_SHAREHOUSE'))
CHANNEL_ID_SIOKONBU = int(os.getenv('SERVER_CHANNEL_ID_SIOKONBU'))

class NotificationClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} (通知クライアント) としてログインしました')
        channel = self.get_channel(CHANNEL_ID_SHAREHOUSE)
        await channel.send("📢 鯖閉じたよ～ ⛔")
        channel = self.get_channel(CHANNEL_ID_SIOKONBU)
        await channel.send("📢 鯖閉じたよ～ ⛔")
        await self.close()  # メッセージ送信後にクライアントを閉じる

if __name__ == "__main__":
    client = NotificationClient(intents=discord.Intents.default())
    client.run(TOKEN)
