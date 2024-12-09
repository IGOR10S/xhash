# xhash

The xhash script computes the hash of strings or files using a user-specified algorithm (supported by the Python hashlib library). Useful for checking data integrity or generating unique identifiers.

## Clona repository

## Rendere xhash eseguibile da qualsiasi percorso

Per eseguire lo script da qualsiasi percorso, devi aggiungere il suo percorso alla variabile di ambiente PATH del sistema operativo oppure configurarlo come eseguibile globale. Ecco i passaggi che puoi seguire su Linux/macOS e Windows.

### Linux/macOS

1. Rendi lo script eseguibile:

    ```bash
    chmod +x xhash.py  # chmod 755 xhash.py
    ```

    Questo comando concede permessi di lettura, scrittura, ed esecuzione al proprietario e solo lettura ed esecuzione agli altri utenti.

2. Sposta lo script in una directory del PATH:

    Copia o sposta il file in una directory già presente nella variabile `PATH`, come `/usr/local/bin` o `$HOME/.local/bin`:

    ```bash
    mv xhash.py /usr/local/bin/xhash
    ```

    Ora puoi eseguire lo script semplicemente digitando `xhash`.

3. Aggiungi una directory personalizzata al PATH:

    Se preferisci utilizzare una directory personalizzata (ad esempio, `$HOME/scripts`):
    1. Crea la directory e sposta il file:

        ```bash
        mkdir -p $HOME/scripts
        mv hash_tool.py $HOME/scripts/hash_tool
        ```

    2. Aggiungi la directory al `PATH` nel file `~/.bashrc` o `~/.zshrc`:

        ```bash
        export PATH="$HOME/scripts:$PATH"
        ```

    3. Ricarica il file di configurazione:

        ```bash
        source ~/.bashrc
        ```

    Ora puoi eseguire il tuo script da qualsiasi percorso nel terminale o prompt dei comandi digitando semplicemente:

    ```bash
    hash_tool -t s -a sha256 -v "Hello, World!"
    ```

### Windows

1. Sposta lo script in una directory del PATH:

    Copia il file dello script in una directory che è già inclusa nella variabile `PATH` di Windows, come:
    - `C:\Users\<tuo_nome_utente>\AppData\Local\Programs\Python\Python<versione>\Scripts`
    - Oppure una directory a tua scelta che aggiungerai al `PATH`.

2. Aggiungi una directory personalizzata al PATH:

    - Crea una directory, ad esempio, `C:\scripts`.
    - Copia lo script in questa directory.
    - Aggiungi questa directory al `PATH`:
        1. Premi `Win + R`, digita `sysdm.cpl` e premi `Invio`.
        2. Vai alla scheda **Avanzate** e clicca su **Variabili d'ambiente**.
        3. Nella sezione **Variabili di sistema**, seleziona la variabile `Path` e clicca su **Modifica**.
        4. Clicca su **Nuovo** e inserisci il percorso della directory (`C:\scripts`).
        5. Clicca su **OK** per salvare.

3. Rendi lo script eseguibile senza `python`:

    Cambia l'estensione del file in `.bat` o `.cmd`:
    - Crea un file `xhash.bat` nella stessa directory:

        ```bat
        @echo off
        python "C:\scripts\xhash.py" %*
        ```

    Ora puoi eseguire lo script da qualsiasi percorso digitando `xhash`.

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

Installa dos2unix:

```bash
sudo dnf install dos2unix  # Fedora
sudo apt install dos2unix  # Ubuntu/Debian
```

Utilizza il comando dos2unix per convertire il file:

```bash
dos2unix xhash.py
```

Se l'errore persiste, verifica di non avere ulteriori caratteri nascosti nel file con:

```bash
cat -A $HOME/.local/bin/xhash
```
