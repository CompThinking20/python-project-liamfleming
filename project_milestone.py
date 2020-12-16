import random

adjective_list = ["hot", "cold", "warm", "soft",  "bright", "dark", "big", "small", "hard", "shocking", "touching", "wet", "dry", "hurting", "fast", "slow", "under", "above", "lower"]
#These sentences/poems are supposed to come from a non-human perspective, so I want all of the adjectives and nouns to be based on complete, simple senses. Nothing that connects to human ideas or constructs, like "beautiful" or "horrible", which implies a stance and oppinion based on the noun that comes from a human's perception of the world.
verb_list = ["run", "jump", "crawl", "pounce", "swim", "lurk", "sleep", "dream", "fuck", "eat", "breathe", "starve", "dive", "growl", "grow", "become", "lose", "find"]
pronoun_list =  ["I", "You", "We"]
noun_list = ["tree", "earth", "sun", "stars", "moon", "noise", "light", "noise-light", "ear", "tail", "paw",  "scale",  "tongue", "mouth", "rock", "mountain", "hole", "whole", "emptiness", "nothing", "space", "center", "heart", "stomach", "tendril", "tooth", ]
connecting_words = ["the"]

adjective = random.choice(adjective_list)
verb = random.choice(verb_list)
pronoun = random.choice(pronoun_list)
noun = random.choice (noun_list)
connect = random.choice (connecting_words)

grammar = [adjective, verb, pronoun, noun, connect]

def sentence_generator(list):
  #The idea behind the sentence generator is to make different building blocks - sentences, or lines (they're serving the same purpose here) - that I can generate randomly and string together into verses, and then into a poem.
  #I decided to use lists as the function's argument, just so I can have one place with all of the words, split into different parts, for the function to pick from. It also helps because now I can make different lists with different types of words - or collections of words with different vibes - and find ways to use multiple, different lists in the poetry generator
  sentence = ((adjective + " " + pronoun + " " + verb + " " + connect + " " + noun))
  #The "sentence" variable marks the order that specific types of words are going to be used in the list, and then put together to make a line or sentence, i.e. an adjective is randomly picked and put in the sentence first, followed by a pronoun, and then a verb and so on. I don't know anything about animal psychology, but I want the order of the words to be based on the order that different parts of information - the immediate senses, processed into the person, and then the action - are transmitted to the brain.
  return sentence
  print(sentence)

word1 = random.choice(grammar)
word2 = random.choice(grammar)
word3 = random.choice(grammar)
word4 = random.choice(grammar)
word5 = random.choice(grammar)

lines = [1, 2, 3, 4]


chaos_sentence = word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5

words = [word1, word2, word3, word4, word5]

also_sentence = pronoun + " " + verb + " " + " " + connect + " " + noun

another_sentence = connect + " " + noun + " " + pronoun + " " + verb + " " + adjective

sentence_chaos = random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words)

sentence = ((adjective + " " + pronoun + " " + verb + " " + connect + " " + noun))

aanother_sentence = pronoun + " " + connect + " " + adjective + " " + noun


all_sentences = [sentence, also_sentence, another_sentence, aanother_sentence]

def multi_sentence(list):
  print(random.choice(all_sentences))
  print(random.choice(all_sentences))
  print(random.choice(all_sentences))
  print(random.choice(all_sentences))



  
  def another_one(list):
  print(random.choice(all_sentences))
  print(random.choice(some_sentences))
  print(chaos_sentence)
  print(sentence)


def a_little_poem(list):
  print(multi_sentence(grammar))
  print(another_one(grammar))

print(a_little_poem(grammar))
