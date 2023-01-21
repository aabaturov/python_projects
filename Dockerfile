FROM python
COPY bot.py /app/
COPY config.py /app/
COPY sendings.py /app/
COPY stickers /app/stickers
RUN pip install pyTelegramBotAPI
WORKDIR /app/
CMD ["python3","bot.py"]
