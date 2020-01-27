from chatterbot import ChatBot



# Create a new instance of a ChatBot
bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        # # no real service url provided
        # {
        #     'import_path': 'services.MyLogicAdapter'
        # },
        {
            'import_path': 'logic_adapter.MyLogicAdapter'
        }


    ]
)

# print(bot.get_response('what is the confidence?').confidence)

print(bot.get_response('what is temperature').text)