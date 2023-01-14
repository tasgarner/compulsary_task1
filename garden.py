# importing modules
import spacy
nlp = spacy.load('en_core_web_sm')

# creating list of garden path sentences
gardenpathSentences = ["The President of the USA which had been struggling with high unemployment rates announced a new stimulus package for businesses",
"The man who hunts ducks out on weekends",
"The cotton clothing is made of grows in Mississippi.",
"Mary the dog bit the child who was given a plaster.",
"The board of directors for Google who were discussing the new budget in the conference room voted on the acquisition of another company"]

# using for loop to read each sentence individually before tokenising and identifying entities
for i, sentence in enumerate(gardenpathSentences):
    doc = nlp(sentence)
    print("Tokens:")
    print([token.orth_ for token in doc])
    print("Entities:")
    print([(ent.text, ent.label_) for ent in doc.ents])
    print("\n")

# i found the entities 'PERSON' and 'ORG' were unusual to me as i did not expect all names
# to be recognised as a person, and for company names to be immediately identified as organisations