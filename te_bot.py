import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

commands = {
    'token': 'Our token is the JRT.',
    'whykyc': "Jarvis Exchange is a fully regulated exchange with a fat gateway. We take utmost care with our customers"
              " security and we want to take all AML precautions we can. For your comfort and the safety of everyone on"
              " our platform, we ask you to go through a KYC procedure with our trusted third party.",
    'kyc': 'All investors must go through KYC - our KYC procedure is done by a trusted third party',
    'kycdocs': 'You can take a photo with your phone or scan the documents.',
    'whatkycdocs': 'This depends on your nationality and location. Once you start creating your profile, the platform'
                   ' will ask your nationality and ask you for the documents you need to provide, based on this'
                   ' information.',
    'whymanywallets': 'In the Jarvis centralized exchange needs to be structured with multiple wallets to help reduce'
                      ' risk and to comply with various regulations.  Despite having multiple wallets there will be '
                      'a smart display function which will only display total assets and their allocation within '
                      'different wallets. So, from a design point of view, you still get full interoperability. '
                      'However, from regulative and technical point of view, splitting the wallets allows everything '
                      'to be by the books and to function at full capacity. Clever, right?',
    'mainwallet': 'It’s the traditional main checking account where funds are deposited/ withdrawn and provides a high'
                  ' level of access. The Main Wallet is a “hot” wallet that can accept and hold both Fiat and '
                  'Digital Currencies.',
    'tradingwallet': 'The Trading Wallet is a special wallet separate from main wallet with enhanced security features'
                     ' that is capable of escrow like functionality. It is not possible to deposit or withdraw funds '
                     'from this wallet to a non-Jarvis wallet. It is only possible to move funds to other Jarvis'
                     ' wallets or to place trades on digital assets. This wallet only allows trading with a 1:1 '
                     'leverage ratio.',
    'marginwallet': 'The Margin Wallet is very similar to the Trading Wallet however it will allow trading of digital'
                    ' assets with leverage, and will also allow the collateralization of assets to facilitate margin'
                    ' and leveraged trading of digital and traditional products such as FX and CFDs. It is expected '
                    'that in the future this wallet functionality is going to be merged together with the Trading '
                    'Wallet as soon as regulations allow for such functionality to be enabled.',
    'holdingwallet': 'The Holding Wallet could be viewed as a highly-secured vault and an alternative to self-managed'
                     ' cold storage. While the highest level of security of funds is generally considered to be'
                     ' for the user to put their funds in Cold Storage, the Holding Wallet provides an alternative'
                     ' additional level of security compared to most other wallet options. A user who would like to '
                     'secure his assets can select from the services of an external partner company to put their '
                     'holdings in an audited cold storage solution.  There are several such solutions which allow '
                     'for holdings in both digital currency or physical assets such as Gold, Silver, Oil, etc...',
    'spending wallet': 'The Spending Wallet will be similar to an active checking or cash bank account. It will be'
                       ' from here that funds will be accessible for spending by the Jarvis debit card, partner debit'
                       ' card, or directly on the users Smartphone using NFC technology. This wallet will need to be'
                       ' different from the previous wallets to ensure compliance with existing regulations.  This will'
                       ' also allow for the functionality to lock exchange rates for holdings on some blockchains.  '
                       'This wallet will be a key component in making blockchain usable by the masses.  It is expected '
                       'that many of the functions and capabilities of this wallet will be greatly enhanced or '
                       'supported through partnerships and collaboration with external partners. In summary, this '
                       'wallet allows for connection to physical card solutions from Visa or MasterCard as well as '
                       'digital spending /payment apps.'

}

updater = Updater(token='679961016:AAGMwNyzeHmLj4IegESYm8YvQTvDXy-Cr-I')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def genericHandlerImpl(bot, update):
    print(update.message)
    question = update.message.text[1:]
    bot.send_message(chat_id=update.message.chat_id, text=commands[question])

genericHandler = CommandHandler(commands.keys(), genericHandlerImpl)
dispatcher.add_handler(genericHandler)

def start(bot, update):
    #chat id is "557478733"
    bot.send_message(chat_id=update.message.chat_id, text="Hi, I'm a bot! How can I help?")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand!")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
