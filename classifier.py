import sys

def classify_and_reply(message):
    message_lower = message.lower()
    
    # Правила классификации по ключевым словам
    if any(word in message_lower for word in ['справк', 'где', 'парковк']):
        category = 'Справка'
        if 'справк' in message_lower:
            reply = "Здравствуйте! Вы можете заказать справку о месте учёбы в личном кабинете студента или обратиться в деканат."
        elif 'парковк' in message_lower:
            reply = "Здравствуйте! Гостевая парковка находится справа от главного входа, для въезда нужен пропуск."
        else:
            reply = "Здравствуйте! Пожалуйста, уточните ваш справочный вопрос."
            
    elif any(word in message_lower for word in ['очередь', 'холодная', 'пропал', 'wi-fi', 'wi‑fi']):
        category = 'Жалоба'
        if 'wi-fi' in message_lower or 'wi‑fi' in message_lower or 'пропал' in message_lower:
            reply = "Приносим извинения! Мы уже передали заявку в IT-отдел, скоро интернет будет восстановлен."
        else:
            reply = "Приносим извинения за доставленные неудобства. Мы уже передали информацию руководству столовой для решения проблемы."
            
    else:
        category = 'Другое'
        reply = "Здравствуйте! Оставьте свои контактные данные, и специалист свяжется с вами для записи и уточнения времени."
            
    return category, reply

def main():
    try:
        with open('messages.txt', 'r', encoding='utf-8') as f:
            messages = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print("Ошибка: не удалось прочитать файл messages.txt")
        return
        
    print("=== Классификатор обращений ===\n")
    for msg in messages:
        # Убираем нумерацию из начала строки для чистоты обработки (например, "1) ")
        clean_msg = msg.split(')', 1)[-1].strip() if ')' in msg else msg
        
        category, reply = classify_and_reply(clean_msg)
        
        print(f"Сообщение: {clean_msg}")
        print(f"Категория: {category}")
        print(f"Ответ: {reply}")
        print("-" * 50)

if __name__ == '__main__':
    main()
