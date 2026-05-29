@echo off
cd /d "C:\Users\chron\Desktop\github\backup\Seraphine"

REM Verifica se o ambiente Conda já existe
conda env list | findstr "seraphine" >nul
if %errorlevel% neq 0 (
    echo Criando ambiente Conda...
    conda create -y -n seraphine python=3.8
)

echo Ativando ambiente Conda...
call conda activate seraphine

echo Instalando dependências...
pip install -r requirements.txt

echo Iniciando Seraphine...
python main.py
