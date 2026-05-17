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

**Chat messages used in both tests:**

![Terminal chat](screenshots/Screenshot_2026-05-17_104444.png)

**Without encryption — message content fully visible in the packet:**

![Plaintext packet 1](screenshots/Screenshot_2026-05-17_104044.png)
![Plaintext packet 2](screenshots/Screenshot_2026-05-17_104107.png)

**Code change made to disable encryption for the demo:**

![Code with encryption commented out](screenshots/Screenshot_2026-05-17_104213.png)

**With RSA encryption — 128 bytes of unreadable ciphertext:**

![Encrypted packet 1](screenshots/Screenshot_2026-05-17_105219.png)
![Encrypted packet 2](screenshots/Screenshot_2026-05-17_105231.png)
