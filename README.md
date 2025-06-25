# iykyk
stock trading strategy (quantitative trading)

# How to set up
1. setup WSL or you can straightaway jump to step 2
2. Download Ollama and run the LLM model locally
```bash
ollama run llama2
```
3. create python virtual env
```bash
python3 -m venv venv
```
4. activate the env
```bash
source .venv/bin/activate
```
5. deactivate using
```bash
deactivate
```
6. install the packages
```bash
pip3 install -r requirements.txt
```
7. done, you are good to go

# Debug
export the packages to a txt file to be installed later
```bash
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```
Make your terminal better <br>
![image](https://github.com/user-attachments/assets/2af837ef-3a12-4a6f-b32c-e4d8873c6d9f)

# The ingredients

#### Stock market data
https://www.financialdatasets.ai/

#### Stock knowledge
https://www.youtube.com/watch?v=T37YvxMTofc

#### LLM
Ollama (llama2) <br>
https://www.youtube.com/watch?v=UtSSMs6ObqY

#### Inspired by
https://github.com/virattt/ai-hedge-fund

#### Python
Python 3.10.12

#### WSL
Ubuntu 22.04

#### MacOS
Sequoia 15.5
