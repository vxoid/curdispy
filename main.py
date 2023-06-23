import curdis, time,  asyncio, json
TOKEN = "MTA5MDI0Mzk2Njc3Mjk4NTg5Nw.GTciW2.Z9_PLAPyDuRoMKZuN8iZSduFNtLPFXZcelydG4"
bot = curdis.DiscordAPI(token=TOKEN)
channel_id = "1086953979948314694"

def delete_all_messages():
    messages = bot.get_all_messages(channel_id=channel_id)
    print(len(messages))
    i = 0
    while i < len(messages):
        print(f"deleting {messages[i].get_content()}")
        messages[i].delete()
        time.sleep(0.5)
        print(len(messages))
        i+=1

def delete_curse():
    with open('equipment/curse.json', 'r') as file:
        curse = json.load(file)
    while True:
        time.sleep(0.5)
        messages = bot.get_all_messages(channel_id=channel_id)
        for message in messages:
            m = message.get_content()
            for c in curse:
                if c in m.lower() and message.get_usr_id() != bot.app_id:
                    message.delete()
                    print('deleting message')
                    time.sleep(0.4)
                    try:
                        if 'бан' in m.lower():
                            print('lox was banned')
                            message.kick_member()
                            message.send_message()
                    except Exception as a:
                        print(f"failed banned\n{a}")
                        bot.send_message("бачу маєш адмінку какіш😈", channel_id=channel_id)


delete_curse()

# curse = "fuck shit dick bitch pussy stupid fucking блять сука підор гандон ганвнюк чмо какіш бан нахуй "
# c = curse.split()
# with open('equipment/curse.json', 'w', encoding='utf-8') as file:
    # json.dump(c, file, ensure_ascii=False)

# with open("cum.mp4", "rb") as file:
#     f = file.read()
# bot.send_message(channel_id="1086953979948314694",  files=f)

# b= bot.get_all_messages(channel_id=channel_id)
# for m in b:
#     m.send_message()



# botik = ws.WSBot()
# async def handle_message(id, content,):
#     print(f"Received message: {content}")
#     pass
# command_handlers = {
#     # "command_name": command_handler_function,
# }
# asyncio.run(botik.run(handle_message))