#! python3
# randomQuizGenerator.py tworzy quiz wraz z pytaniami i odpowiedziami
# ułożonymi w losowej kolejności wraz z odpowiedziami

import random

# Dane quizu: nazwy województw z ich miastami wojewódzkimi (stolicami)

stolice = { 'dolnośląskiego': 'Wrocław',
            'kujawsko-pomorskiego':'Bydgoszcz',
            'lubeskiego': 'Lublin',
            'lubuskiego': 'Gorzów Wielkopolski',
            'łódzkiego': 'Łódz',
            'małopolskiego': 'Kraków',
            'mazowieckiego':'Warszawa',
            'opolskiego': 'Opole',
            'podkarpackiego': 'Rzeszów',
            'podlaskiego': 'Białystok',
            'pomorskiego': 'Gdańsk',
            'śląskiego': 'Katowice',
            'świętokrzyskiego': 'Kielce',
            'warmińsko-mazurskiego': 'Olsztyn',
            'wielkopolskiego': 'Poznań',
            'zachodniopomorskiego': 'Szczecin'
           }

# Wygenerowanie 35 plików quizu

for quizNum in range(10):
    # Utworzenie plików quizu i odpowiedzi na pytania
    quizFile = open (f'województwa_quiz{quizNum + 1}.txt','w')
    answerKeyFile = open(f'województwa_answers{quizNum + 1}.txt', 'w')
    
    # Zapis nagłówka quizu

    quizFile.write('Imie i Nazwisko:\n\nData:\nKlasa:\n\n')
    quizFile.write((' '*20) + f'Quiz stolic wojedzództw (Quiz {quizNum +1})' )
    quizFile.write('\n\n')
    
    # Losowe ustawienie koleności województw

    województwa = list(stolice.keys())
    random.shuffle(województwa)

    # Iteracja przez 16 województw

    for questionNum in range(16):
        # Przygotowanie prawidłowych i nieprawidłowych odpowiedzi
        correctAnswer = stolice[województwa[questionNum]]
        wrongAnswers = list(stolice.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
    
        # Zapis pytania i odpowiedzi w pliku quizu

        quizFile.write(f'{questionNum +1}. Co jest stolicą województwa {województwa[questionNum]}?\n')
        for i in range(4):
            quizFile.write('    %s. %s\n' %  ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Zapis odpowiedzi w pliku

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
