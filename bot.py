import sys
import re

def load_faq(filepath):
    qa_pairs = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip().split('\n\n')
            for block in content:
                lines = block.strip().split('\n')
                if len(lines) >= 2:
                    q = lines[0].replace('Вопрос:', '').strip()
                    a = '\n'.join(lines[1:]).replace('Ответ:', '').strip()
                    qa_pairs.append({'q': q, 'a': a})
    except Exception as e:
        print(f"Ошибка чтения {filepath}: {e}")
        sys.exit(1)
    return qa_pairs

def get_answer(question, qa_pairs):
    question = question.lower()
    
    # Ключевые слова для 5 тем
    keywords_map = [
        (['врем', 'когда', 'во скольк', 'расписани', 'начал', 'конец'], 0), # время
        (['команд', 'человек', 'участник', 'состав'], 1), # команда
        (['трек', 'направлен', 'выбор'], 2), # трек
        (['сдач', 'сдавать', 'сдать', 'загруз', 'git', 'репозитори', 'отправ'], 3), # сдача
        (['приз', 'побед', 'выигр', 'мерч', 'наград'], 4) # призы
    ]
    
    for keywords, index in keywords_map:
        for kw in keywords:
            if kw in question:
                if index < len(qa_pairs):
                    return qa_pairs[index]['a']
                
    # Если совпадений по ключевым словам нет, ищем пересечения слов с самими вопросами
    words = set(re.findall(r'[а-яa-z0-9]+', question))
    max_match = 0
    best_answer = "Не знаю."
    
    for pair in qa_pairs:
        q_words = set(re.findall(r'[а-яa-z0-9]+', pair['q'].lower()))
        match_count = len(words.intersection(q_words))
        if match_count > max_match:
            max_match = match_count
            best_answer = pair['a']
            
    if max_match > 0:
        return best_answer

    return "не знаю"

def main():
    print("🤖 Бот запущен! Задайте вопрос о репетиции хакатона.")
    print("Напишите 'выход' для завершения.\n")
    
    qa_pairs = load_faq('faq.txt')
    if not qa_pairs:
         print("Файл faq.txt пуст или имеет неверный формат.")
         return

    while True:
        try:
            user_input = input("Вы: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ['выход', 'exit', 'quit']:
                print("Бот: Пока!")
                break
                
            answer = get_answer(user_input, qa_pairs)
            print(f"Бот: {answer}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nБот: Пока!")
            break

if __name__ == "__main__":
    main()
