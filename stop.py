import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv(override=True)  # 環境変数を上書きするために override=True を指定
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_BOOT_CHANNEL_ID = int(os.getenv('SERVER_CHANNEL_ID'))

class NotificationClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} (通知クライアント) としてログインしました')
        channel = self.get_channel(SERVER_BOOT_CHANNEL_ID)
        await channel.send("📢 鯖閉じたよ～ ⛔")
        await self.close()  # メッセージ送信後にクライアントを閉じる

async def main():
    client = NotificationClient(intents=discord.Intents.default())
    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
