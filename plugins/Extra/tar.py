from pyrogram import Client, filters


@bot.on.message(filters.command('fars') )
def command1(bot, message):
message.reply_text("Hello help")

print ("i am helping")
