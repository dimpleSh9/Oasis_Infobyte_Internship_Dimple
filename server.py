import socket
import threading


HOST = '127.0.0.1'
PORT = 1234
Server_limit = 3
Active_users = []


def listen_for_messages(client, username):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':

            final_msg = username + '-:' + message
            messagesToAll(final_msg)

        else:
            print(f"The message sent from the client {username} is enpty")


def send_message_to_client(client, message):
    client.sendall(message.encode())


def messagesToAll(message):
    for user in Active_users:
        send_message_to_client(user[1], message)


def client_handle(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            Active_users.append((username, client))
            server_message = "SERVER-:" + f"{username} is added to the chat." 
            messagesToAll(server_message)
            break

        else:
            print('Client username is enpty')
    threading.Thread(target=listen_for_messages, args=(client, username)).start()


def main():
    #socket class object creation
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to Host {HOST} and Port {PORT}.")
    
    server.listen(Server_limit)

    while 1:
        client , address = server.accept()
        print(f"Successfully connected to {address[0]} {address[1]}")

        threading.Thread(target= client_handle, args = (client,)).start()


if __name__ == "__main__":
    main()
