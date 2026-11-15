
## Ferramenta para automatizar a instalação e compilação do **QSocket** e do **GSocket** em dispositivos Android com Termux (AArch64).

# Projetos

- [QSocket](https://github.com/qsocket/qsocket)
- [GSocket](https://gsocket.io/)

## Requisitos

- Python
- git (opcional)
## antes de instalar:

- pkg update && pkg upgrade -y
- pkg install python -y

## deploy one line:
gsocket: wget https://raw.githubusercontent.com/theendofabbys/socket64/refs/heads/main/gsocket/main.sh && chmod +x main.sh && ./main.sh



qsocket: wget https://raw.githubusercontent.com/theendofabbys/socket64/refs/heads/main/qsocket/main.py && python main.py

uso Qsocket: qsock --help


## Compatibilidade

Testado em Termux com arquitetura Aarch64

