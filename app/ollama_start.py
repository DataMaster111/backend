from openai import OpenAI

# Настройка клиента OpenAI для работы с локальным Ollama
client = OpenAI(
    base_url="http://localhost:11434/v1",  # URL Ollama
    api_key="ollama"  # Фиктивный ключ для Ollama
)

# Создание запроса к модели
response = client.chat.completions.create(
    model="yandex/YandexGPT-5-Lite-8B-instruct-GGUF",  # Модель, загруженная через Ollama
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain local AI deployment benefits"}
    ]
)

# Вывод ответа
print(response.choices[0].message.content)
# Пример использования Ollama с OpenAI API
# Убедитесь, что Ollama запущена и модель YandexGPT загружена
# Запустите Ollama с помощью команды: ollama serve
