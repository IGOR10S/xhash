# xhash

A script that computes the hash of strings or files using a user-specified algorithm (supported by the Python **hashlib** library). Useful for checking data integrity or generating unique identifiers.

## Clone the repo

```bash
git clone https://github.com/IGOR10S/xhash.git
cd xhash
```

## Add to the PATH

### Linux

```bash
chmod +x xhash.py
mv xhash.py /usr/local/bin/xhash
```

> [!TIP]
> To print the contents of the environment variable `PATH` on Linux, use `echo $PATH`.

### Windows 11

Move the script to a directory included in the Windows environment variable `PATH`, such as `C:\Users\<your_user_name>\AppData\Local\Programs\Python\Python<version>\Scripts`, or create one and add it to PATH with the command `setx PATH "%PATH%;C:\Path\to\dir`.

> [!TIP]
> To print the contents of the environment variable `PATH` on Windows 11 use either `echo %PATH%` (Command Prompt) or `$Env:PATH`(PowerShell).

Crea un file `xhash.bat` (o `xhash.cmd`) nella stessa directory per rendere lo script eseguibile senza digitare `python3`.

```bat
@echo off
python "C:\Path\to\dir\xhash.py" %*
```

## Run script

```bash
xhash -h
```

Now you can start the script just typing `xhash` everywhere.

## Problemi noti

```bash
$ xhash 
/usr/bin/env: ‘python3\r’: No such file or directory
/usr/bin/env: use -[v]S to pass options in shebang lines
$
```

> [!CAUTION]
> Questo errore viene riscontrato a causa dalla presenza di caratteri di fine riga in stile Windows (`\r\n`) nel file invece dei caratteri di fine riga in stile Unix (`\n`). Questo può succedere se il file è stato creato o modificato su Windows e poi trasferito su Linux senza conversione.

### Soluzione

Installa **dos2unix**:

```bash
sudo dnf install dos2unix  # Fedora
sudo apt install dos2unix  # Ubuntu/Debian
```

Utilizza il comando `dos2unix` per convertire il file:

```bash
dos2unix xhash.py
```

Se l'errore persiste, verifica di non avere ulteriori caratteri nascosti nel file con:

```bash
cat -A /usr/local/bin/xhash
```
