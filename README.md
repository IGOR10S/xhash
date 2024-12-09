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
> Per stampare il contenuto della variabile d'ambiente `PATH` su Linux utilizza `echo $PATH`.

### Windows 11

Sposta lo script in una directory inclusa nella variabile d'ambiente `PATH` di Windows, come `C:\Users\<tuo_nome_utente>\AppData\Local\Programs\Python\Python<versione>\Scripts`, oppure creane una e aggiungila a PATH con il comando `setx PATH "%PATH%;C:\Path\to\dir`.

> [!TIP]
> Per stampare il contenuto della variabile d'ambiente `PATH` su Windows 11 utilizza `echo %PATH%` (Prompt dei comandi) o `$Env:PATH` (PowerShell).

Rendi lo script eseguibile senza `python`:

- Crea un file `xhash.bat` (o `xhash.cmd`) nella stessa directory:

    ```bat
    @echo off
    python "C:\scripts\xhash.py" %*
    ```

## Run script

```bash
xhash -h
```

Now you can start the script just typing `xhash` everywhere.

## Problemi noti

> [!CAUTION]
>
> ```bash
> $ xhash 
> /usr/bin/env: ‘python3\r’: No such file or directory
> /usr/bin/env: use -[v]S to pass options in shebang lines
> $
> ```
>
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
cat -A $HOME/.local/bin/xhash
```
