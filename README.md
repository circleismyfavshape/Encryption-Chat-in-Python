# Encryption Chat in Python

A peer-to-peer terminal chat application with end-to-end RSA encryption built using Python sockets. Captured and verified encrypted vs plaintext traffic using Wireshark.

## Stack
- Python (`socket`, `threading`, `rsa`)
- Wireshark for network traffic analysis

## What it does
- Connects two clients over TCP
- Generates a 1024-bit RSA key pair on startup and exchanges public keys before any messages are sent
- Encrypts all outgoing messages with the partner's public key
- Decrypts incoming messages with the local private key

## Wireshark Verification
Captured the same conversation twice — once without encryption and once with — to confirm that RSA ciphertext is unreadable over the wire compared to plaintext.

### 1. Both sides of the chat — host and client exchanging messages used in the Wireshark capture
<img width="1910" height="220" alt="terminal_chat_both_sides" src="https://github.com/user-attachments/assets/8ae32a5e-da00-47a8-b5e4-e7d345fa7193" />

### 2. Without encryption — the full message `"I like playing volleyball, even though I suck at it"` is readable as plaintext directly in the Wireshark packet
<img width="1599" height="899" alt="wireshark_plaintext_packet1" src="https://github.com/user-attachments/assets/a0612666-e5b5-4ac7-aee9-80bbc03faeec" />

### 3. Without encryption — the second message `"My secret is that I hate lemons, but I am afraid to admit that."` also fully exposed in the packet data
<img width="1599" height="899" alt="wireshark_plaintext_packet2" src="https://github.com/user-attachments/assets/c6e9859a-6561-4e61-9f88-5311b8de0a25" />

### 4. Code change made to demonstrate the unencrypted version — RSA encrypt/decrypt calls commented out and replaced with raw `send`/`recv`
<img width="770" height="272" alt="code_encryption_disabled" src="https://github.com/user-attachments/assets/009d8cec-8025-4333-a46c-2ce31f77e4b2" />

### 5. With RSA encryption enabled — the same message is now 128 bytes of unreadable ciphertext, no plaintext visible anywhere in the packet
<img width="1599" height="899" alt="wireshark_encrypted_packet1" src="https://github.com/user-attachments/assets/bd4cc2aa-640b-41f4-9b06-813284e47c90" />

### 6. With RSA encryption enabled — second message also fully hidden, fixed 128-byte ciphertext block regardless of original message length
<img width="1599" height="899" alt="wireshark_encrypted_packet2" src="https://github.com/user-attachments/assets/05b12c22-3cf1-466a-9cf7-4c3741665ec8" />
