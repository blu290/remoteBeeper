import asyncio
import uuid
#command prefix will be "+ijz0vpkNYmqru/BiUmx1w=="
#messages will be in the format:authenticate command arguments
connected_clients = {}

async def handle_client(reader,writer):
    global connected_clients
    todelete = []
    client_id = str(uuid.uuid4())
    connected_clients[client_id] = writer

    data = await reader.read(100)
    message = data.decode()
    command = message.split(" ")
    command_len = len(command)

    if command_len >= 1 and command[0] == "+ijz0vpkNYmqru/BiUmx1w==":
        #print("received command")               #handle commands from the control bot
        if command_len >=4 and command[1] == "beep":
            for id,client_writer in connected_clients.items():
                messageStr = command[1] + " " + command[2] + " " + command[3]
                print(messageStr)
                try:
                    if id != client_id:
                        client_writer.write(messageStr.encode())
                        await client_writer.drain()
                except Exception as e:
                    todelete.append(id)
            #broadcast a beep to all users
            for x in todelete:
                del connected_clients[x]
        writer.write("0".encode())
    else:
        #print("not supposed to be here")
        writer.write("-1".encode())
    await writer.drain()

async def main():
    server = await asyncio.start_server(handle_client,port=8008)
    print("started server")
    async with server:
        await server.serve_forever()
asyncio.run(main())