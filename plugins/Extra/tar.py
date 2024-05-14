from pyrogram import Client, filters


@Client.on_message(filters.command("fars"))
def command1(bot, message):
message.reply_text("Hello fars")

print ("i am helping")
