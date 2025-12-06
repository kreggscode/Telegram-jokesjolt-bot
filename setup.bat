@echo off
echo ========================================
echo   Telegram Jokes Bot - Quick Setup
echo ========================================
echo.

REM Check if .env exists
if exist .env (
    echo [OK] .env file found
) else (
    echo [!] Creating .env file...
    echo # Telegram Bot Configuration > .env
    echo BOT_TOKEN=your_bot_token_here >> .env
    echo CHAT_ID=your_channel_chat_id_here >> .env
    echo. >> .env
    echo # Timezone Configuration (offset from UTC in hours) >> .env
    echo # Examples: 5.5 for IST, -5 for EST, 0 for UTC >> .env
    echo TIMEZONE_OFFSET_HOURS=5.5 >> .env
    echo.
    echo [!] .env file created! Please edit it with your credentials.
    echo.
    echo How to get your credentials:
    echo   BOT_TOKEN: Message @BotFather on Telegram
    echo   CHAT_ID: Run 'python get_chat_id.py' after setting BOT_TOKEN
    echo.
    pause
    exit /b
)

echo.
echo Step 1: Installing dependencies...
echo ========================================
python -m pip install --upgrade pip -q
pip install -r requirements.txt -q

echo.
echo Step 2: Running configuration test...
echo ========================================
python test_bot_config.py

echo.
echo ========================================
echo Setup complete!
echo ========================================
pause
