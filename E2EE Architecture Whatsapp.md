# Complete End-to-End Encryption (E2EE) Architectural Flow

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                         END-TO-END ENCRYPTION (E2EE) ARCHITECTURE                             │
└──────────────────────────────────────────────────────────────────────────────────────────────┘


                                      INITIAL SETUP
                                           │
                                           ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                           SENDER / ALICE DEVICE                                                │
│                                                                                              │
│  Generate / store cryptographic identity material                                             │
│                                                                                              │
│  ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────────┐     │
│  │ Identity Key Pair    │     │ Signed Prekey Pair   │     │ One-Time Prekey Pairs    │     │
│  │                      │     │                      │     │                          │     │
│  │ Public Key           │     │ Public Key           │     │ Public Keys              │     │
│  │ Private Key          │     │ Private Key          │     │ Private Keys             │     │
│  └──────────────────────┘     └──────────────────────┘     └──────────────────────────┘     │
│                                                                                              │
│  Private keys remain protected on the endpoint.                                              │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               │ Public key material
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      KEY SERVER /                                              │
│                                  PREKEY DIRECTORY                                              │
│                                                                                              │
│  Stores / distributes public key material:                                                    │
│                                                                                              │
│  • Identity Public Key                                                                         │
│  • Signed Prekey                                                                               │
│  • Signature on Signed Prekey                                                                  │
│  • One-Time Prekeys                                                                            │
│                                                                                              │
│  The server does NOT receive the corresponding private keys.                                  │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               │ Bob's public key bundle
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                  SESSION ESTABLISHMENT                                          │
│                                                                                              │
│  Alice retrieves Bob's public key material.                                                   │
│                                                                                              │
│  Alice verifies the Signed Prekey signature using Bob's Identity Public Key.                 │
│                                                                                              │
│  This helps authenticate the public key material before key agreement.                        │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                              AUTHENTICATED KEY AGREEMENT                                       │
│                                                                                              │
│                         DIFFIE–HELLMAN / ELLIPTIC-CURVE DH                                    │
│                                                                                              │
│       ALICE                                                               BOB                 │
│       ─────                                                               ───                 │
│                                                                                              │
│       Alice Private Key: a                                  Bob Private Key: b               │
│       Alice Public Key: A = aG                              Bob Public Key: B = bG            │
│              │                                                               │                │
│              │────────────── Exchange public values ────────────────────────►│                │
│              │                                                               │                │
│              │◄─────────────────────────────────────────────────────────────│                │
│                                                                                              │
│       Alice computes:                                      Bob computes:                     │
│                                                                                              │
│       S = aB                                               S = bA                              │
│         = a(bG)                                              = b(aG)                         │
│         = abG                                                 = abG                          │
│                                                                                              │
│                         SAME SHARED SECRET MATERIAL                                           │
│                                  S = abG                                                       │
│                                                                                              │
│       The private values are NEVER transmitted.                                               │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               │ Shared secret material
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                              KEY DERIVATION FUNCTION (KDF)                                    │
│                                                                                              │
│  Shared Secret + Protocol Context / Additional Secret Inputs                                 │
│                         │                                                                      │
│                         ▼                                                                      │
│               ┌───────────────────────┐                                                        │
│               │         KDF           │                                                        │
│               │ Key Derivation        │                                                        │
│               │ Function              │                                                        │
│               └───────────┬───────────┘                                                        │
│                           │                                                                    │
│                           ▼                                                                    │
│                     ROOT KEY (RK)                                                              │
│                           │                                                                    │
│                           ▼                                                                    │
│                    CHAIN KEY (CK)                                                              │
│                           │                                                                    │
│                           ▼                                                                    │
│                    MESSAGE KEY (MK)                                                            │
│                                                                                              │
│  The shared secret is generally NOT used directly as the message encryption key.             │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                              DOUBLE RATCHET / KEY EVOLUTION                                    │
│                                                                                              │
│                         ┌───────────────────────────┐                                         │
│                         │       ROOT KEY            │                                         │
│                         └─────────────┬─────────────┘                                         │
│                                       │                                                       │
│                          Symmetric-key ratchet                                                │
│                                       │                                                       │
│                                       ▼                                                       │
│                         ┌───────────────────────────┐                                         │
│                         │       CHAIN KEY           │                                         │
│                         └─────────────┬─────────────┘                                         │
│                                       │                                                       │
│                    ┌──────────────────┼──────────────────┐                                    │
│                    ▼                  ▼                  ▼                                    │
│              MESSAGE KEY 1      MESSAGE KEY 2      MESSAGE KEY 3       ...                   │
│                    │                  │                  │                                    │
│                    ▼                  ▼                  ▼                                    │
│                 Msg 1              Msg 2              Msg 3                                  │
│                                                                                              │
│  A new message key is derived for successive messages.                                       │
│                                                                                              │
│  Periodically / when protocol state requires:                                                │
│                                                                                              │
│                    New DH Key Pair                                                            │
│                           │                                                                    │
│                           ▼                                                                    │
│                  Diffie-Hellman Ratchet                                                      │
│                           │                                                                    │
│                           ▼                                                                    │
│                     New Root Key                                                              │
│                           │                                                                    │
│                           ▼                                                                    │
│                  New Chain Keys                                                               │
│                                                                                              │
│  This key evolution provides properties such as forward secrecy and                          │
│  post-compromise recovery under the protocol's security assumptions.                         │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                  USER WRITES MESSAGE                                           │
│                                                                                              │
│                          "Hello Bob!"                                                         │
│                               │                                                              │
│                               ▼                                                              │
│                         PLAINTEXT (P)                                                         │
│                                                                                              │
│  Plaintext exists locally on Alice's device before encryption.                               │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                             MESSAGE ENCRYPTION STAGE                                          │
│                                                                                              │
│  Plaintext (P)                                                                               │
│       +                                                                                      │
│  Message Key (MK)                                                                            │
│       +                                                                                      │
│  Nonce / IV (N)                                                                              │
│       +                                                                                      │
│  Associated Data (AAD)                                                                       │
│       │                                                                                      │
│       ▼                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐     │
│  │                       AEAD ENCRYPTION                                                │     │
│  │                                                                                     │     │
│  │       Authenticated Encryption with Associated Data                                │     │
│  │                                                                                     │     │
│  │       Examples: AES-GCM / ChaCha20-Poly1305                                         │     │
│  └───────────────────────────────────────┬─────────────────────────────────────────────┘     │
│                                          │                                                   │
│                                          ▼                                                   │
│                        ┌─────────────────────────────────┐                                   │
│                        │          CIPHERTEXT (C)         │                                   │
│                        │                                 │                                   │
│                        │          +                      │                                   │
│                        │                                 │                                   │
│                        │   AUTHENTICATION TAG (T)        │                                   │
│                        │                                 │                                   │
│                        │          +                      │                                   │
│                        │                                 │                                   │
│                        │          NONCE (N)               │                                   │
│                        └─────────────────────────────────┘                                   │
│                                                                                              │
│  Conceptual encryption:                                                                      │
│                                                                                              │
│       (C, T) = AEAD_Encrypt(MK, N, P, AAD)                                                   │
│                                                                                              │
│  Encryption happens BEFORE the message leaves Alice's device.                               │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               │ Ciphertext + metadata
                                               ▼
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║                                      NETWORK                                                 ║
║                                                                                              ║
║       Internet / Wi-Fi / Mobile Network / Routers / ISP                                      ║
║                                                                                              ║
║                         Intermediaries see encrypted data                                    ║
╚══════════════════════════════════════════════╤═══════════════════════════════════════════════╝
                                               │
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   MESSAGING SERVER                                             │
│                                                                                              │
│  Receives:                                                                                   │
│       • Ciphertext                                                                            │
│       • Authentication Tag                                                                    │
│       • Nonce / Protocol Metadata                                                             │
│                                                                                              │
│  Server responsibilities:                                                                     │
│       • Message routing                                                                       │
│       • Delivery                                                                              │
│       • Temporary storage / offline queuing                                                   │
│       • Device/session management                                                             │
│                                                                                              │
│  Server normally DOES NOT possess:                                                           │
│       • Message encryption key                                                                │
│       • Recipient's private key                                                               │
│       • Sender's private key                                                                  │
│                                                                                              │
│                       Therefore:                                                             │
│                                                                                              │
│                  CIPHERTEXT ───────────────► CIPHERTEXT                                      │
│                                                                                              │
│             Server forwards encrypted data rather than plaintext.                            │
└──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                               │
                                               │ Ciphertext delivery
                                               ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                  RECIPIENT / BOB DEVICE                                        │
│                                                                                              │
│                       Receive encrypted message                                              │
│                               │                                                              │
│                               ▼                                                              │
│                     Parse protocol metadata                                                   │
│                               │                                                              │
│                               ▼                                                              │
│                Determine receiving chain / ratchet state                                      │
│                               │                                                              │
│                               ▼                                                              │
│                     Derive / retrieve MESSAGE KEY                                             │
│                               │                                                              │
│                               ▼                                                              │
│                    Obtain corresponding key material                                          │
│                               │                                                              │
│                               ▼                                                              │
│                     AUTHENTICATION CHECK                                                       │
│                               │                                                              │
│                     ┌─────────┴─────────┐                                                     │
│                     │                   │                                                     │
│                  VALID               INVALID                                                   │
│                     │                   │                                                     │
│                     ▼                   ▼                                                     │
│              Continue to           Reject / fail                                              │
│              decryption            authentication                                             │
│                     │                                                                       │
│                     ▼                                                                       │
│        ┌───────────────────────────────────────────┐                                          │
│        │             AEAD DECRYPTION               │                                          │
│        │                                           │                                          │
│        │  Ciphertext + Message Key + Nonce + AAD  │                                          │
│        │                   │                       │                                          │
│        │                   ▼                       │                                          │
│        │              PLAINTEXT                    │                                          │
│        └──────────────────────┬────────────────────┘                                          │
│                               │                                                              │
│                               ▼                                                              │
│                         "Hello Bob!"                                                         │
│                               │                                                              │
│                               ▼                                                              │
│                     MESSAGE DISPLAYED                                                        │
└──────────────────────────────────────────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                              COMPLETE SECURITY MODEL                                          │
│                                                                                              │
│   IDENTITY AUTHENTICATION                                                                     │
│          │                                                                                   │
│          ▼                                                                                   │
│   KEY AGREEMENT                                                                               │
│          │                                                                                   │
│          ▼                                                                                   │
│   SHARED SECRET                                                                               │
│          │                                                                                   │
│          ▼                                                                                   │
│   KEY DERIVATION                                                                               │
│          │                                                                                   │
│          ▼                                                                                   │
│   MESSAGE-SPECIFIC KEYS                                                                       │
│          │                                                                                   │
│          ▼                                                                                   │
│   AUTHENTICATED ENCRYPTION                                                                    │
│          │                                                                                   │
│          ▼                                                                                   │
│   CIPHERTEXT                                                                                    │
│          │                                                                                   │
│          ▼                                                                                   │
│   UNTRUSTED / INTERMEDIARY SERVER                                                              │
│          │                                                                                   │
│          ▼                                                                                   │
│   AUTHENTICATION + KEY DERIVATION                                                              │
│          │                                                                                   │
│          ▼                                                                                   │
│   DECRYPTION                                                                                   │
│          │                                                                                   │
│          ▼                                                                                   │
│   PLAINTEXT ONLY AT ENDPOINT                                                                   │
│                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Key Technical Terms

| Term                         | Meaning                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| **Plaintext**                | Original readable message                                                               |
| **Ciphertext**               | Encrypted unreadable representation of the message                                      |
| **Public Key**               | Key that can be distributed publicly                                                    |
| **Private Key**              | Secret key that must remain protected                                                   |
| **Identity Key**             | Long-term key used to represent a cryptographic identity                                |
| **Prekey**                   | Public key material that enables asynchronous session establishment                     |
| **Ephemeral Key**            | Temporary cryptographic key                                                             |
| **Key Agreement**            | Process through which endpoints independently derive shared secret material             |
| **Diffie-Hellman (DH)**      | Cryptographic key-agreement mechanism                                                   |
| **KDF**                      | Key Derivation Function; derives cryptographic keys from secret material                |
| **Root Key**                 | Ratchet state used to derive subsequent chain keys                                      |
| **Chain Key**                | Key-derivation state used to generate message keys                                      |
| **Message Key**              | Key used for an individual message encryption/decryption operation                      |
| **Double Ratchet**           | Protocol mechanism combining symmetric-key and DH ratchets                              |
| **AEAD**                     | Authenticated Encryption with Associated Data                                           |
| **Nonce**                    | Value used by an encryption operation according to the cipher's uniqueness requirements |
| **AAD**                      | Data authenticated but not encrypted                                                    |
| **Authentication Tag**       | Cryptographic value used to verify integrity/authenticity                               |
| **Forward Secrecy**          | Limits exposure of past messages after certain later key compromises                    |
| **Post-Compromise Recovery** | Ability of a ratcheting protocol to regain security after certain compromises           |
| **Ciphertext Transmission**  | Encrypted data travelling through the network                                           |
| **Endpoint**                 | Sender or recipient device where plaintext encryption/decryption occurs                 |
| **Server**                   | Intermediate system responsible for routing/storing encrypted messages                  |

```

**For your GitHub README:** this single flowchart can be your main architecture section. It contains the full chain from **key generation → prekeys → authentication → DH key agreement → shared secret → KDF → Double Ratchet → message key → AEAD encryption → ciphertext → server → key derivation → authentication → decryption → plaintext**, so it should work well for both documentation and viva preparation.
```
