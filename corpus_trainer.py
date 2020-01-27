from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pickle
chatbot = ChatBot('Training Example', read_only=True)       # read_only = True disables reinforced learning
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

# trainer.train(
#     "chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations"
# )

print(chatbot.get_response('hi'))
