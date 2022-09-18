# we take a look at SSH

**SSH** is a **Secure Shell protocol** used as the primary means of connecting to Linux servers remotely providing a text-based interface by spawning a remote shell. After connecting, all commands you type in your local terminal are sent to the remote server and executed there.

In order to connect to a remote server, we need to generate key pair:
 - private key
 - public key (*.pub*)
 This is done using the command
 ```sh
 $ ssh-keygen
 ```
 
 ---
**NOTE**

To learn more about ssh and ssh-keygen respectively, checkout their manuals

```sh
man ssh
```
```sh
man ssh-keygen
```

---
