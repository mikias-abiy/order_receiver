# Order receiver

## Description

This a simple telegram bot that automates the hustle of regestering orders manualy by showing available items and letting user register their orders by giving them a serious of prompots. Even though the prompots are specific to the items that I was selling at the time I built this project you can tweak it a little to make it meat your needs. Don't hesatet to do so because it's well documented and organized. Checkout the [dive deep into the inner working of the bot](#how-it-works).

# Installation

First Clone the repo using this command.
```
git clone https://github.com/mikias-abiy/order_receiver.git
```
Then, Navigate to the directory you cloned.
```
cd order_receiver
```

Then create a python virtual enviroment. It's recommended to use virtual enviroment to not mess with the version of other projects dependencies (but keep in mind this optional)
```
python3 -m venv .venv
```

Then activate the virtual enviroment by executing this command (assuming you are using linux)
you can look the documentation for venv [here](https://docs.python.org/3/library/venv.html).
```
. .venv/bin/activate
```

Then, install all the necessary third party libraries by executing the following command.
```
pip install -r requirements.txt
```

Then, set the your bot's token in the config.py file ot the `BOT_API_TOKEN` variable. If you don't have or don't know how to generate Telegram bot API token take a look at there documentation [here](https://core.telegram.org/bots/tutorial#obtain-your-bot-token)

Then, run the bot by executing the following command
```
python3 main.py
```


