# Introduccion a los Chatbots

Codigo correspondiente a la presentacion de Introduccion a los Chatbos en le marco de Cafeto XP

En este repositorio encontraras

-[01_reglas](01_reglas): Una lista de tareas hecha con reglas
-[02_chatterbot](02_chatterbot): Un bot conversacional usando Chatterbot
-[03_rasa_list](03_rasa_list): Una re implementacion de la lista de tareas usando [Rasa](https://rasa.com/)
-[04_rasa_bot](04_rasa_bot): Un chatbot que usa el gestor de dialogos de RASA

## Instalando Rasa

### Prerequisitos

Asegurese de tener [bazel](https://bazel.build/) y [tensorflow](https://www.tensorflow.org/?hl=es-419) Instalados

En ubuntu

```bash
# You need postgres
sudo apt install libpq-dev
# Bazel
sudo apt install apt-transport-https curl gnupg
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install bazel
pip install tensorflow==2.3.4
```

```bash
pip install rasa
```

