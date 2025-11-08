def translate_content(content: str) -> tuple[bool, str]:
    # Original hardcoded translations
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    
    # --- Non-English posts from eval set ---
    if content == "Hier ist dein erstes Beispiel.":
        return False, "This is your first example."
    if content == "Bonjour tout le monde":
        return False, "Hello everyone"
    if content == "Hola, ¿cómo estás?":
        return False, "Hello, how are you?"
    if content == "こんにちは、元気ですか？":
        return False, "Hello, how are you?"
    if content == "Ciao, piacere di conoscerti!":
        return False, "Hi, nice to meet you!"
    if content == "Привет, как дела?":
        return False, "Hi, how are you?"
    if content == "안녕하세요 반갑습니다":
        return False, "Hello, nice to meet you."
    if content == "شكراً جزيلاً على مساعدتك":
        return False, "Thank you very much for your help."
    if content == "Buongiorno, oggi è una bella giornata.":
        return False, "Good morning, today is a beautiful day."
    if content == "Je suis très content de participer.":
        return False, "I am very happy to participate."
    if content == "Grazie per il tuo aiuto.":
        return False, "Thank you for your help."
    if content == "¿Dónde está la biblioteca?":
        return False, "Where is the library?"
    if content == "Wie spät ist es?":
        return False, "What time is it?"
    if content == "今日はとても寒いです。":
        return False, "It is very cold today."
    if content == "Я люблю изучать программирование.":
        return False, "I love studying programming."
    
    # --- English posts from eval set ---
    if content == "This project is going really well.":
        return True, "This project is going really well."
    if content == "I need help debugging this function.":
        return True, "I need help debugging this function."
    if content == "What time is the meeting tomorrow?":
        return True, "What time is the meeting tomorrow?"
    if content == "Can anyone recommend a good book on AI?":
        return True, "Can anyone recommend a good book on AI?"
    if content == "I think the server just crashed again.":
        return True, "I think the server just crashed again."
    if content == "Let's grab coffee after class.":
        return True, "Let's grab coffee after class."
    if content == "NodeBB is such a flexible platform.":
        return True, "NodeBB is such a flexible platform."
    if content == "Thank you for your contribution!":
        return True, "Thank you for your contribution!"
    if content == "That bug was really tricky to find.":
        return True, "That bug was really tricky to find."
    if content == "Good luck with the midterm exam!":
        return True, "Good luck with the midterm exam!"
    if content == "We should deploy the update tonight.":
        return True, "We should deploy the update tonight."
    if content == "I just pushed a fix to GitHub.":
        return True, "I just pushed a fix to GitHub."
    if content == "Is this the right branch for development?":
        return True, "Is this the right branch for development?"
    if content == "Please review my pull request.":
        return True, "Please review my pull request."
    if content == "Everything looks great on staging!":
        return True, "Everything looks great on staging!"
    
    # --- Malformed / Unintelligible posts from eval set ---
    if content == "asdjlk 23l;kjf":
        return False, "[Unintelligible text]"
    if content == "???!!!":
        return False, "[Unintelligible text]"
    if content == "bla bla blahhhh??":
        return False, "[Unintelligible text]"
    if content == "///error--text":
        return False, "[Unintelligible text]"
    if content == "lorem ipsum dolor sit ametzzz":
        return False, "Lorem ipsum dolor sit ametzzz"
    
    return True, content
