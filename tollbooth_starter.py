import phantom_tollbooth
import cleaners as cl # all functions


def main():
    book = phantom_tollbooth.get_text()
    cl.calculate_word_frequency()

if __name__ == '__main__':
    main()