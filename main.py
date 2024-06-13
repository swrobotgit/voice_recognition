import vosk
import sys
import os
import pyaudio

# Устанавливаем модель для русского языка
model = vosk.Model("vosk-model-small-ru-0.22")

# Создаем объект распознавания речи
rec = vosk.KaldiRecognizer(model, 16000)


# Функция для распознавания речи с микрофона
def recognize_speech():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    while True:
        data = stream.read(4000)
        # print(data)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            print(result)
            if "шрек" in result:
                print("Илюха Шрек")

    result = rec.FinalResult()
    if "Илья" in result:
        print("Илья")

    stream.stop_stream()
    stream.close()
    p.terminate()


# Запускаем распознавание речи
recognize_speech()
