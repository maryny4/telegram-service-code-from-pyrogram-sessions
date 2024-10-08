---

# Telegram Authorization Code Fetcher

This project is a simple script for automatically retrieving Telegram login codes from sessions using the Pyrogram library. It listens to incoming messages from Telegram's official number (777000) and extracts the login code using a regular expression. Once the code is found, it is saved to a file for each phone number.

## Features

- **Session Management**: Automatically starts Pyrogram clients using pre-existing session files stored in the `sessions` folder.
- **Telegram Code Parsing**: Listens for incoming messages from the Telegram bot (user 777000) and extracts the login code using a regex pattern.
- **Code Storage**: Saves extracted login codes to the `codes` folder, with each code stored in a file named after the corresponding phone number.
- **Multiple Sessions**: Handles multiple sessions simultaneously by creating a Pyrogram client for each `.session` file found in the `sessions` folder.
- **Graceful Shutdown**: Supports stopping all running clients with user input.

## Parameters

In the script, replace the following values with your own `api_id` and `api_hash` from Telegram:

```python
api_id = 1488
api_hash = "1488"
```

These values are required for the Pyrogram clients to interact with Telegram's API.

## How It Works

1. **Initialize Clients**: The script scans the `sessions` folder for `.session` files and initializes a Pyrogram client for each one.
2. **Listen for Messages**: Each client listens for messages from the Telegram bot (777000), which contains the login code.
3. **Extract Login Code**: The login code is extracted using a regex pattern from the incoming message.
4. **Save Login Code**: The extracted code is saved in the `codes` folder, named after the phone number (the session file name).
5. **Stop the Clients**: All clients can be stopped by pressing Enter in the console.

### Example of Code Extraction

When the script successfully retrieves a Telegram login code, it will display output like this:

```
Код 23213 для номера 573225883230 сохранен в файл codes\573225883230.code
```

## Folder Structure

- **sessions/**: This folder contains the `.session` files used by Pyrogram to manage Telegram accounts.
- **codes/**: This folder stores the extracted login codes, with each file named after the corresponding phone number.

## Requirements

- Python 3.7+
- `pyrogram` library

You can install the required library with:
```bash
pip install pyrogram
```

## How to Use

1. Place the `.session` files (generated with Pyrogram) in the `sessions` folder.
2. Run the script using:
   ```bash
   python script_name.py
   ```
3. The script will launch Pyrogram clients and listen for login codes. Once a code is received, it will be saved in the `codes` folder.
4. To stop all clients, simply press Enter in the console.

## Example of Telegram Code Message
The script expects the Telegram login code to be in the following format:
```
Login code: 12345
```

## License

This project is open-source under the MIT License.

---

Это описание включает обновлённые параметры `api_id` и `api_hash`, а также пример вывода для сообщений с кодами Telegram.
