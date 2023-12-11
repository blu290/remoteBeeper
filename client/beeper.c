#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock.h>
#include <windows.h>
#include <pthread.h>
#define MAX_BUFFER_SIZE 1024
#define IP "31.205.17.161"
#define PORT (8008)

void* serverCommunication(void* arg) {
    SOCKET clientSocket = *(SOCKET*)arg;

    while (1) {
        char buffer[MAX_BUFFER_SIZE];
        int bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);
        int duration,frequency;
        if (bytesRead > 0) {
            buffer[bytesRead] = '\0';

            //printf("Received: %s\n", buffer);
            //printf("%s\n",buffer);
            if(sscanf(buffer, "beep %d %d",&duration, &frequency) == 2){
                Beep(frequency,duration*1000);
            }
            // Check if the message is "beep" and play the sound

        } else {
            printf("Connection closed by the server.\n");
            break;
        }
    }

    return NULL;
}
int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        fprintf(stderr, "Failed to initialize winsock.\n");
        return 1;
    }

    SOCKET clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == INVALID_SOCKET) {
        fprintf(stderr, "Failed to create socket.\n");
        WSACleanup();
        return 1;
    }

    // Set up the server address and port
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT); // Replace YourServerPort with the actual port
    serverAddr.sin_addr.s_addr = inet_addr(IP); // Replace YourServerAddress with the actual address

    // Connect to the server
    if (connect(clientSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        fprintf(stderr, "Failed to connect to the server.\n");
        closesocket(clientSocket);
        WSACleanup();
        return 1;
    }

    printf("Connected to the server.\n");

    // Create a thread for server communication
    pthread_t thread;
    if (pthread_create(&thread, NULL, serverCommunication, &clientSocket) != 0) {
        fprintf(stderr, "Failed to create thread.\n");
        closesocket(clientSocket);
        WSACleanup();
        return 1;
    }

    // Wait for the server communication thread to finish
    pthread_join(thread, NULL);

    // Cleanup
    closesocket(clientSocket);
    WSACleanup();

    return 0;
}