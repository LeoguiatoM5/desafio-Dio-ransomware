# Desafio Simulação Ransomware - DIO

# Simulação de Ransomware 🛡️

Este projeto é uma **simulação educacional de ransomware**, demonstrando como arquivos podem ser criptografados e descriptografados utilizando o módulo `cryptography` em Python. O objetivo é ilustrar o funcionamento de um ransomware de forma ética e responsável.

## ⚠️ Aviso
Este código é exclusivamente para fins educacionais e demonstração. Não deve ser usado para atividades maliciosas ou ilegais.

---

## 🔑 Tipo de Criptografia

O projeto utiliza a **criptografia simétrica** com a biblioteca `cryptography` e o módulo `Fernet`. Nesse método:
- Uma única chave é gerada e usada tanto para criptografar quanto para descriptografar os dados.
- A chave é armazenada em um arquivo chamado `key.key`.

---

## 🚀 Passo a Passo para Executar

1. **Clone o repositório**:
   ```bash
   git clone git@github.com:LeoguiatoM5/desafio-Dio-ransomware.git
   cd simulacao-ransomware

   🚀 Passo a Passo para Executar

# Criptografar e Descriptografar Arquivos

## **Criptografar um Arquivo**

1. Execute o script `encrypt.py`:

   python encrypt.py
Quando solicitado, insira o nome do arquivo que será criptografado (incluindo a extensão).

O programa realizará os seguintes passos:

Gerar uma chave de criptografia e salvá-la no arquivo key.key.
Criptografar o arquivo especificado.
Sobrescrever o arquivo original com os dados criptografados.
Após a execução, o arquivo estará criptografado.

Descriptografar um Arquivo
Certifique-se de que o arquivo key.key gerado anteriormente está na mesma pasta do projeto.

Execute o script decrypt.py:

python decrypt.py
Quando solicitado, insira o nome do arquivo criptografado que deseja descriptografar (incluindo a extensão).

O programa realizará os seguintes passos:

Carregar a chave de criptografia do arquivo key.key.
Descriptografar o arquivo especificado.
Sobrescrever o arquivo criptografado com os dados originais.
Após a execução, o arquivo será restaurado ao seu estado original.

