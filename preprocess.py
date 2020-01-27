from chatterbot import ChatBot

# preprocessors can be creatied with i/p statement and returns statement instance
def to_lower(statement):
    statement.text = statement.text.lower()
    return statement


chatbot = ChatBot(
    'Bob the Bot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'preprocess.to_lower'
    ]
)

print(chatbot.get_response('  hi   '))