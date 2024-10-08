import os
import asyncio
import threading
import re
from pyrogram import Client, filters

api_id = 1488
api_hash = "1488"

sessions_folder = "sessions"
codes_folder = "codes"

if not os.path.exists(codes_folder):
    os.makedirs(codes_folder)

session_files = os.listdir(sessions_folder)
clients = []
stop_event = threading.Event()

async def run_client(session_name):
    app = Client(session_name, api_id=api_id, api_hash=api_hash)
    clients.append(app)

    @app.on_message(filters.user(777000))
    def handle_message_from_user(client, message):
        # Searching for the code using a regular expression
        code_match = re.search(r'Login code: (\d+)', message.text)
        if code_match:
            code = code_match.group(1)
            phone_number = os.path.basename(session_name)  # Extracting session name (phone number)
            code_file = os.path.join(codes_folder, f"{phone_number}.code")
            with open(code_file, "w") as file:
                file.write(code)
            print(f"Code {code} for the number {phone_number} saved in file {code_file}")

    try:
        await app.start()
        await asyncio.Event().wait()
    finally:
        await app.stop()

async def stop_clients():
    for client in clients:
        await client.stop()

def wait_for_stop():
    input()
    stop_event.set()

async def main():
    tasks = []

    threading.Thread(target=wait_for_stop).start()

    for session_file in session_files:
        if session_file.endswith('.session'):
            session_name = os.path.splitext(os.path.join(sessions_folder, session_file))[0]  # Remove only the extension
            tasks.append(run_client(session_name))

    await asyncio.gather(*tasks)

    await asyncio.get_event_loop().run_in_executor(None, stop_event.wait)

    await stop_clients()

    print(f"Clients started: {len(clients)}")

if __name__ == "__main__":
    asyncio.run(main())
