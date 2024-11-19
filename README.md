# Flight Delay - Predição de Voos

## Descrição Geral

O **Flight Delay - Predição de Voos** é um projeto que utiliza dados reais da ANAC (Agência Nacional de Aviação Civil) sobre voos partindo do Brasil para destinos nacionais e internacionais. O objetivo é analisar e prever atrasos e cancelamentos, considerando fatores como datas, horários, e condições climáticas nos locais de partida e chegada.

Este projeto integra dados históricos de voos com informações meteorológicas para treinar modelos de machine learning, auxiliando na previsão de atrasos e otimizando processos relacionados à aviação.

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento.
- **FastAPI**: Criação de APIs rápidas e eficientes.
- **TensorFlow**: Treinamento de modelos de machine learning.
- **MLFlow**: Gerenciamento de experimentos de machine learning.
- **MongoDB**: Banco de dados para armazenamento dos dados processados.
- **Ubuntu 24.4**: Sistema operacional para execução do projeto.
- **Pandas**: Manipulação e análise de dados.
- **Scikit-Learn**: Implementação de algoritmos de machine learning.

---

## Instalação

### Pré-requisitos

- **Python 3.10+**
- **MongoDB** instalado e configurado.
- Dependências do projeto listadas no arquivo `requirements.txt`.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/flight-delay-prediction.git
   cd flight-dela

2. Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências:

bash

pip install -r requirements.txt
4. Configure as variáveis de ambiente para conexão com o MongoDB e APIs externas (se necessário).

Como Usar
Treinamento do Modelo
Certifique-se de que o banco de dados contém os dados necessários.
Execute o script de treinamento:
bash
Copiar código
python train_model.py
Use o MLFlow para monitorar os experimentos e comparar os modelos.
API de Previsão
Inicie o servidor FastAPI:

bash
Copiar código
uvicorn app.main:app --reload
Acesse a documentação interativa no endereço:

arduino
Copiar código
http://127.0.0.1:8000/docs
Envie uma requisição POST para prever atrasos, incluindo dados do voo e clima no corpo da requisição:

json
Copiar código
{
    "flight_data": {
        "departure": "2024-11-15T08:00:00",
        "arrival": "2024-11-15T10:30:00",
        "origin": "GRU",
        "destination": "GIG"
    },
    "weather_data": {
        "origin": {
            "temperature": 25,
            "precipitation": 0
        },
        "destination": {
            "temperature": 28,
            "precipitation": 5
        }
    }
}
Estrutura de Arquivos
plaintext
Copiar código
flight-delay-prediction/
├── app/
│   ├── main.py        # Arquivo principal da API FastAPI
│   ├── models/        # Modelos para previsões
│   ├── routers/       # Rotas da API
├── data/
│   ├── raw/           # Dados brutos da ANAC e clima
│   ├── processed/     # Dados processados e prontos para uso
├── notebooks/         # Jupyter Notebooks para análise exploratória
├── train_model.py     # Script de treinamento do modelo
├── requirements.txt   # Dependências do projeto
├── README.md          # Documentação
Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

perl
Copiar código

Agora é só colar esse conteúdo no arquivo `README.md` no diretório principal do seu projeto e adicionar ao GitHub com os comandos:

```bash
git add README.md
git commit -m "Adiciona o README do projeto"
git push origin main# FlightBrDelayPredict
