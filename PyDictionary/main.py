import requests


class dictionary():

  def __init__(self):
    print('Welcome to the Dictionary Wrapper Python App')
    print()
    self.URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

  def setWord(self, word):
    self.word = word

  def getInfoOfWord(self):
    self.URLData = requests.get(f'{self.URL}{self.word}')
    self.URLDataJson = self.URLData.json()

  def phonetics(self):
    # Extract phonetics
    if 'license' in self.URLDataJson[0]:
      self.phoneticsData = self.URLDataJson[0]['phonetics']
      print(
          'The Text and Audio URL are as stated below for pronunciation of the word',
          self.word)
      for key in self.phoneticsData:
        if 'license' in key:
          # print(key['text'] if 'text' in key else self.word)
          print('Text -', key.get('text', self.word))
          print('Audio URL -', key.get('audio', 'No audio found'))
          print()
    else:
      print('word not found try google search')

  def definitionWord(self):
    # Extract Definitions
    if 'license' in self.URLDataJson[0]:
      self.meaningData = self.URLDataJson[0]['meanings']
      print('The meaning of the word', self.word, 'in different contexts is')
      for key in self.meaningData:
        # print(key['text'] if 'text' in key else self.word)
        print('Part of Speech -',
              key.get('partOfSpeech', 'General Definition').upper())
        for i in key['definitions']:
          print('Definition -', i['definition'])
          print(
              'Synonyms -', ', '.join(i['synonyms'])
              if i['synonyms'] != [] else 'No Synonyms in this context')
          print(
              'Antonyms -', ', '.join(i['antonyms'])
              if i['antonyms'] != [] else 'No Antonyms in this context')
          print(
              'Simple Example -',
              i['example'] if 'example' in i else 'No Example in this context')
          print()
        print('****' * 10)
        print()
    else:
      print('word not found try google search')

  def wrongData(self):

    # Extract phonetics
    self.googleURL = 'https://www.google.com/search?q='
    if self.URLData.status_code != 200:
      print()
      print(f'''
      Word not found in Dictionary App
      Kindly try with a different word or use Google Search link below
      {self.googleURL}{self.word}''')
    else:
      self.phonetics()
      self.definitionWord()


def main():
  ds = dictionary()
  ch = 'y'
  while ch.lower() == 'y':
    word = input(
        'Enter the word that you want to search in the Dictionary App ')
    print()
    ds.setWord(word)
    ds.getInfoOfWord()
    ds.wrongData()
    print()
    ch = input('Do you want to search more (Y/N)?')
  print('Thanks for using Python Dictionary App')


if __name__ == '__main__':
  main()
