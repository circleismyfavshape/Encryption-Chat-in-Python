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
<img alt="terminal_chat_both_sides" src="screenshots/terminal_chat_both_sides.png" />

### 2. Without encryption — the full message `"I like playing volleyball, even though I suck at it"` is readable as plaintext directly in the Wireshark packet
<img alt="wireshark_plaintext_packet1" src="screenshots/wireshark_plaintext_packet1.png" />

### 3. Without encryption — the second message `"My secret is that I hate lemons, but I am afraid to admit that."` also fully exposed in the packet data
<img alt="wireshark_plaintext_packet2" src="screenshots/wireshark_plaintext_packet2.png" />

### 4. Code change made to demonstrate the unencrypted version — RSA encrypt/decrypt calls commented out and replaced with raw `send`/`recv`
<img alt="code_encryption_disabled" src="screenshots/code_encryption_disabled.png" />

### 5. With RSA encryption enabled — the same message is now 128 bytes of unreadable ciphertext, no plaintext visible anywhere in the packet
<img alt="wireshark_encrypted_packet1" src="screenshots/wireshark_encrypted_packet1.png" />

### 6. With RSA encryption enabled — second message also fully hidden, fixed 128-byte ciphertext block regardless of original message length
<img alt="wireshark_encrypted_packet2" src="screenshots/wireshark_encrypted_packet2.png" />
