@echo off

REM Navigate to the directory where the script is located
cd /d %~dp0

REM Run the Streamlit app
streamlit run app.py

pause
