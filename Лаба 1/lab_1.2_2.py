File = open('readFile', 'r')

wordsInFile = File.read().split(', ') # Формирование списка из файла
uniqWords = [] # Список уникальных слов
numOfWords = [] # Список с количеством вхождений каждого уникального слова

for i in range(len(wordsInFile)): # Формирование списка уникальных слов
    if wordsInFile[i] not in uniqWords:
        uniqWords.append(wordsInFile[i])

for i in range(len(uniqWords)): # Подсчёт каждого уникального слова
    num = 0
    for j in range(len(wordsInFile)):
        if wordsInFile[j] == uniqWords[i]:
            num += 1

    numOfWords.append(num)
    num = 0

print("Число вхождений каждого слова из файла 'readFile':")

for k in range(len(uniqWords)): #Вывод числа вхождений каждого слова
    print(uniqWords[k], "=", numOfWords[k])

File.close()