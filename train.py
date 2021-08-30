from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")
#train the chatter bot for english
trainer.train("data/greetings.yml")
trainer.train("data/myown.yml")