import curdis
TOKEN = "token"
bot = curdis.DiscordAPI(token=TOKEN)

@bot.command("hello")
def say_hi():
    return "Hi there!"

@bot.message_handler()
def msg_handler(message: curdis.Message):
    print(f"msg content: {message.get_content()}")

bot.listen()