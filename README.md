# Portfólio – Douglas Ferreira

Aplicação web de portfólio profissional desenvolvida em Python com Flask, focada em arquitetura de software, performance e apresentação clara de projetos e habilidades.

## Tecnologias
- Python 3.12
- Flask 3
- Jinja2 (templates)
- Tailwind CSS via CDN
- Gunicorn (produção)
- Docker

---

## Executando localmente

Pré-requisitos:
- Python 3.12 instalado
- `pip` configurado

Passos:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPO.git
cd SEU-REPO

pip install -r requirements.txt
python app.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:5000
```

---

## Executando com Docker (local)

```bash
docker build -t douglas-portfolio .
docker run -p 8000:8000 douglas-portfolio
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

---

## Deploy no Railway

1. Versione o código em um repositório Git (GitHub, GitLab etc.).
2. Garanta que os arquivos abaixo estejam na raiz do projeto:
   - `app.py`
   - `requirements.txt`
   - `Dockerfile`
3. Acesse o painel do Railway e crie um novo projeto via **Deploy from GitHub**.
4. Selecione o repositório deste portfólio.
5. O Railway detectará automaticamente o `Dockerfile` e construirá a imagem.
6. Após o deploy, copie a URL gerada pelo Railway e utilize-a como endereço público do portfólio.

Não é necessário configurar o `PORT` manualmente: o Dockerfile e o `app.py` já estão preparados para usar a variável de ambiente fornecida pela plataforma.
