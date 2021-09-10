from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Simple Bot',
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # database_uri='sqlite:///database.sqlite3'
)


def train(bot):

    trainer = ListTrainer(
        bot
    )
    trainer.train(
        [
            'Hola',
            'Hola',
            'Como estas?',
            'Bien'
        ]
    )
    trainer.train(
        [
            'Hola',
            'Que tal, todo bien',
            'Si, bastante vos',
            'Bien',
            'Me alegro'
        ]
    )
    trainer.train(
        [
            'Saludos',
            'Hola',
            'Que hay de nuevo',
            'Nada',
            'Vale, nos vemos'
        ]
    )
