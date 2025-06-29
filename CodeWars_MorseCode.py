from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip()  # Eliminar espacios extra al principio y al final
    words = morse_code.split('   ')  # Separar palabras
    decoded_words = []

    for word in words:
        letters = word.split()  # Separar letras
        decoded_word = ''.join(MORSE_CODE[letter] for letter in letters)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)