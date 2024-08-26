
<!-- omit in toc -->
# Getting Started with TStickers

Welcome to the TStickers tutorial! Follow these steps to get up and running with TStickers. This
guide will walk you through setting up a Telegram bot, retrieving sticker pack URLs, and using
TStickers to download and convert stickers.

<!-- omit in toc -->
## Table of Contents

- [Step 1 - Send a message to @BotFather](#step-1---send-a-message-to-botfather)
- [Step 2 - Create a File Called 'env'](#step-2---create-a-file-called-env)
- [Step 3 - Get the URL of the Telegram Sticker Pack(s)](#step-3---get-the-url-of-the-telegram-sticker-packs)
	- [Option 1 - Use a Browser and Search for the Pack](#option-1---use-a-browser-and-search-for-the-pack)
	- [Option 2 - Use Telegram](#option-2---use-telegram)
- [Step 4 - Use TStickers](#step-4---use-tstickers)

## Step 1 - Send a message to @BotFather

To start using TStickers, you need to create a Telegram bot. Follow these steps to obtain your bot token:

1. **Create a Telegram Account:** If you don’t already have one, download the Telegram app and sign up.

2. **Contact @BotFather:** Open Telegram and search for the user `@BotFather`. This is the official bot for managing other bots on Telegram.

3. **Create a New Bot:**
   - Send the command `/newbot` to @BotFather.
   - Follow the prompts to provide a name for your bot (e.g., `TestBot`) and a username (e.g., `test_bot`).

4. **Receive Your Token:** @BotFather will reply with a message containing your bot’s API token. Keep this token safe, as you'll need it for the next steps.

   <img src="assets/step1.png" alt="Step 1" width="600">

## Step 2 - Create a File Called 'env'

To store your bot token securely, you need to create a configuration file:

1. **Create the File:**
   - Create a new text file in the same directory where you'll run TStickers.
   - Name the file `env` or `env.txt`.

2. **Add Your Token:**
   - Open the file and paste your bot token into it.

   Example `env.txt`:
   ```txt
   14************
   ```

## Step 3 - Get the URL of the Telegram Sticker Pack(s)

To use TStickers, you'll need the URL of the sticker pack(s) you want to download. You can get this URL in two ways:

### Option 1 - Use a Browser and Search for the Pack

1. **Search for the Sticker Pack:**
   - Open your web browser and search for the sticker pack by name (e.g., `Telegram Donut The Dog`).

   <img src="assets/step3_0.png" alt="Step 3: Part 1" width="300">

2. **Copy the URL:**
   - Find the sticker pack link and copy its URL. It should look something like `https://t.me/addstickers/DonutTheDog`.

### Option 2 - Use Telegram

1. **Find the Sticker Pack:**
   - Open the Telegram app, search for the sticker pack, and open it.

2. **Copy the Link:**
   - Tap on the sticker pack’s name or menu options and select "Share" or "Copy Link" (on mobile devices). The URL will be copied to your clipboard.

   Example URL: `https://t.me/addstickers/DonutTheDog`

   <img src="assets/step3_1.png" alt="Step 3: Part 2" width="300">

## Step 4 - Use TStickers

Now you’re ready to use TStickers to download and convert stickers from the URL you obtained:

1. **Install TStickers:**
   - Run the following command in your terminal:
     ```bash
     python3 -m pip install tstickers
     ```

2. **Run TStickers:**
   - Start the program by executing:
     ```bash
     python3 -m tstickers
     ```

3. **Enter the Sticker Pack URL:**
   - When prompted, paste the URL of the sticker pack and press Enter.

4. **Check the Output:**
   - TStickers will download and convert the stickers. The output will be saved in the `downloads` folder.

   Example output:
   ```bash
   $ tstickers
   Enter sticker_set url (leave blank to stop): https://t.me/addstickers/DonutTheDog
   Enter sticker_set url (leave blank to stop):
   INFO     | ============================================================
   INFO     | Starting to scrape "DonutTheDog" ..
   INFO     | Time taken to scrape 31 stickers - 0.044s
   INFO     |
   INFO     | ------------------------------------------------------------
   INFO     | Starting download of "donutthedog" into downloads\donutthedog
   INFO     | Time taken to download 31 stickers - 0.157s
   INFO     |
   INFO     | ------------------------------------------------------------
   INFO     | -> Cache miss for DonutTheDog!
   INFO     | Converting stickers "DonutTheDog"...
   INFO     | Time taken to convert 31 stickers (tgs) - 60.970s
   INFO     |
   INFO     | Time taken to convert 31 stickers (webp) - 0.447s
   INFO     |
   INFO     | Time taken to convert 62 stickers (total) - 61.434s
   INFO     |
   ```
