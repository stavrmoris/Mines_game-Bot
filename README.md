# 🎰 Mines Game Bot

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-red.svg)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-20.x-green.svg)
![Stars](https://img.shields.io/github/stars/stavrmoris/Mines_game-Bot)

Mines Game Bot is a Telegram bot that provides a fun mines game and signals for users.

[Read in Russian](README_RU.md)

## 📚 Table of Contents

- [Description](#-description)
- [Installation](#-installation)
- [Usage](#-usage)
- [License](#-license)

## 📜 Description

This code implements a Telegram bot that allows users to play a mines game and receive signals. The bot provides an interactive interface with buttons to access instructions and a web application. It uses the `python-telegram-bot` library to interact with the Telegram API.

## 🔧 Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/stavrmoris/Mines_game-Bot.git
    cd Mines_game-Bot
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # on Windows use `venv\Scripts\activate`
    ```

3. **Install the necessary dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Open a main file `main.py` and add your data:**
    ```
    TOKEN=your_telegram_bot_token
    CHANNEL_URL='your_chanel'
    WEB_APP_URL='your_url'
    ```

## 🚀 Usage

1. **Run the bot:**
    ```bash
    python bot.py
    ```

2. **Interact with the bot:**
   - Open Telegram and find your bot by its name.
   - Send the command `/start` to start using the bot.
   - Follow the instructions and play the mines game or get signals.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
