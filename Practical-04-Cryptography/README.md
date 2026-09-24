# Practical 04: Cryptography

## Aim

To study and practically implement basic cryptographic techniques including **encryption, hashing, and digital signatures**, and understand their role in protecting the confidentiality, integrity, and authenticity of data.

## Objectives

* Understand the basic concept of cryptography.
* Perform encryption and decryption using CyberChef.
* Generate a cryptographic hash of a message.
* Understand the difference between encryption and hashing.
* Generate and verify a digital signature.
* Understand the applications of cryptographic techniques in data privacy and security.

## Tool Used

**CyberChef — The Cyber Swiss Army Knife**

Official Website: https://gchq.github.io/CyberChef/

CyberChef is a web-based tool developed by GCHQ that provides operations for encryption, encoding, hashing, data analysis, and other cybersecurity tasks.

## Cryptography Concepts

### 1. Encryption

Encryption converts readable **plaintext** into an unreadable form called **ciphertext** using an algorithm and a key.

The ciphertext can be converted back into plaintext through decryption when the appropriate key is available.

**Purpose:** Confidentiality

Example:

```text
Plaintext → Encryption → Ciphertext
Ciphertext → Decryption → Plaintext
```

### 2. Hashing

Hashing converts data into a fixed-length hash value using a hash algorithm.

Unlike encryption, hashing is designed to be a **one-way process**. The original data is not normally recovered from the hash.

**Purpose:** Integrity and verification

Example:

```text
Message → SHA-256 → Hash Value
```

### 3. Digital Signature

A digital signature is a cryptographic mechanism used to verify the **authenticity and integrity** of digital information.

A private key is used to create a signature, while the corresponding public key can be used to verify it.

**Purpose:**

* Authentication
* Integrity
* Non-repudiation

---

# Experiment 1: Encryption and Decryption

## Objective

To encrypt plaintext and subsequently decrypt the ciphertext using an encryption algorithm.

## Procedure

1. Open CyberChef.
2. Enter the following sample text in the **Input** area:

```text
Data Privacy Practical
```

3. Search for the **AES Encrypt** operation.
4. Add the operation to the Recipe area.
5. Enter a sample key when required.
6. Select the required encryption parameters.
7. Observe the encrypted output.
8. Take a screenshot of the encryption process.
9. Create a second recipe using **AES Decrypt**.
10. Use the same compatible key and parameters.
11. Enter the encrypted output as input.
12. Observe whether the original plaintext is recovered.

## Expected Result

The plaintext should be converted into ciphertext during encryption.

After applying the appropriate decryption operation with the correct key and parameters, the original plaintext should be recovered.

### Observation

| Operation      | Input                  | Output                 |
| -------------- | ---------------------- | ---------------------- |
| AES Encryption | Data Privacy Practical | Encrypted ciphertext   |
| AES Decryption | Encrypted ciphertext   | Data Privacy Practical |

### Screenshot

Save the screenshot as:

```text
screenshots/aes-encryption.png
```

---

# Experiment 2: Hashing Using SHA-256

## Objective

To generate a SHA-256 hash of a given message and understand the use of hashing for data integrity.

## Procedure

1. Open CyberChef.
2. Enter the following text:

```text
Data Privacy Practical
```

3. Search for the **SHA2** operation.
4. Add it to the Recipe area.
5. Select **SHA-256** if the operation provides a choice of SHA-2 variants.
6. Observe the generated hash.
7. Record the output.
8. Change one character in the original message.
9. Generate the SHA-256 hash again.
10. Compare both hash values.

## Expected Result

The two messages should produce different hash values even though only one character was changed.

This demonstrates the sensitivity of cryptographic hashes to changes in the input.

### Observation

| Input                   | Hash Algorithm | Result                         |
| ----------------------- | -------------- | ------------------------------ |
| Data Privacy Practical  | SHA-256        | Hash value generated           |
| Data Privacy Practical. | SHA-256        | Different hash value generated |

### Conclusion

A small change in the input produces a substantially different hash value. Therefore, cryptographic hashing can be used to detect changes to data and verify integrity.

### Screenshot

Save the screenshot as:

```text
screenshots/sha256-hashing.png
```

---

# Experiment 3: Digital Signature

## Objective

To understand the process of creating and verifying a digital signature using public-key cryptography.

## Procedure

1. Open CyberChef.
2. Use a sample message such as:

```text
This document belongs to the Data Privacy practical.
```

3. Explore the available public-key and digital-signature operations.
4. Generate or use a suitable key pair if the selected operation requires one.
5. Use the private key to create a digital signature.
6. Use the corresponding public key to verify the signature.
7. Record the result of the verification.
8. Modify the original message.
9. Attempt verification again.
10. Observe the difference in the verification result.

## Expected Result

The original message should be successfully verified when the corresponding valid signature and key are used.

If the message is modified after signing, the signature should no longer validate the modified content.

### Observation

| Condition                             | Verification             |
| ------------------------------------- | ------------------------ |
| Original message + valid signature    | Successful verification  |
| Modified message + original signature | Verification should fail |

### Screenshot

Save the screenshot as:

```text
screenshots/digital-signature.png
```

---

# Comparison of Cryptographic Techniques

| Technique         | Main Purpose                 | Reversible?                                 | Key Required?           |
| ----------------- | ---------------------------- | ------------------------------------------- | ----------------------- |
| Encryption        | Confidentiality              | Yes, with appropriate decryption            | Yes                     |
| Hashing           | Integrity / verification     | No practical reversal                       | No                      |
| Digital Signature | Authentication and integrity | Signature is verified rather than decrypted | Private/public key pair |

---

# Applications

## Encryption

Encryption is commonly used for:

* Protecting confidential files
* Secure communication
* Online banking
* Secure connections
* Protecting stored sensitive information

## Hashing

Hashing is commonly used for:

* Password storage systems
* File integrity verification
* Digital forensics
* Data integrity checks
* Detecting changes in files

## Digital Signatures

Digital signatures are commonly used for:

* Electronic documents
* Software signing
* Digital certificates
* Secure transactions
* Authentication of digital communications

---

# Privacy and Security Relevance

Cryptographic techniques are important components of data protection.

**Encryption** helps prevent unauthorized people from reading confidential information.

**Hashing** helps detect whether information has been modified.

**Digital signatures** help establish that information came from the expected signer and has not been altered after signing.

Together, these techniques contribute to the confidentiality, integrity, and authenticity of digital information.

---

# Result

The practical demonstrated three important cryptographic concepts:

1. Encryption and decryption were studied using CyberChef.
2. SHA-256 hashing was performed and the effect of changing input data was observed.
3. The concept and verification process of digital signatures were studied.

The practical helped demonstrate how cryptographic techniques are used to protect digital information and support data privacy.

---

# Conclusion

Cryptography provides fundamental techniques for protecting digital information. Encryption protects confidentiality, hashing helps maintain integrity, and digital signatures provide authentication and integrity verification.

CyberChef provided a convenient environment for understanding these concepts through practical experimentation without requiring additional software installation.

---

## References

* CyberChef — GCHQ: https://gchq.github.io/CyberChef/
* CyberChef GitHub Repository: https://github.com/gchq/CyberChef

## Academic Note

All experiments in this practical use sample data only. No real passwords, confidential documents, personal information, or sensitive credentials were used.
