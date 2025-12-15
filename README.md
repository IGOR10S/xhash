# xhash

A script that computes the hash of strings or files using a user-specified algorithm (supported by the Python **hashlib** library). Useful for checking data integrity or generating unique identifiers.

## Clone the repo

```bash
git clone https://github.com/IGOR10S/xhash.git
cd xhash
```

## Add to PATH

### Linux

```bash
chmod +x xhash.py
mv xhash.py /usr/local/bin/xhash
```

> [!TIP]
> To print the contents of `PATH` on Linux, use `echo $PATH`.

### Windows 11

1. Move the script to a directory included in the Windows `PATH`, such as `C:\Users\<your_user_name>\AppData\Local\Programs\Python\Python<version>\Scripts`, or create one and add it to PATH with:

    ```bash
    setx PATH "%PATH%;C:\Path\to\dir"
    ```

> [!TIP]
> To print the contents of `PATH` on Windows 11 use either `echo %PATH%` (Command Prompt) or `$Env:PATH` (PowerShell).

2. Create a file `xhash.bat` (or `xhash.cmd`) in the same directory to make the script executable without typing `python3`:

    ```bat
    @echo off
    python3 "C:\Path\to\xhash.py" %*
    ```

## Run script

Now you can start the script by typing `xhash` anywhere:

```bash
xhash -h
```

## Known issues (Linux only)

```bash
/usr/bin/env: ‘python3\r’: No such file or directory
/usr/bin/env: use -[v]S to pass options in shebang lines
```

> [!CAUTION]
> This error is caused by the file having **Windows-style** (`\r\n`) endline characters instead of **Unix-style** (`\n`) endline characters. This can happen if the file was created or modified on Windows and then transferred to Linux without conversion.

### Solution

Install **dos2unix**:

```bash
sudo dnf install dos2unix  # Fedora
sudo apt install dos2unix  # Ubuntu/Debian
```

Start again with [Clone the repo] and convert the file with the command `dos2unix xhash.py` before adding it to the `PATH`.

> [!TIP]
> If the error persists, check to see if you have any more hidden characters in the file with `cat -A /usr/local/bin/xhash`.

<!-- Link -->
[Clone the repo]:https://github.com/IGOR10S/xhash#clone-the-repo
