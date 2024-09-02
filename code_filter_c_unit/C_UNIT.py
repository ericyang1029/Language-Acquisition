import re
import json
from nltk.tokenize import sent_tokenize
from nltk import pos_tag, word_tokenize

# Ensure NLTK resources are available
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
import string

def is_not_punctuation(char):
    """
    Check if the given character is not a punctuation.

    Parameters:
    - char: A single character to check

    Returns:
    - True if the character is not a punctuation, False otherwise
    """
    return char not in string.punctuation

def is_complete_sentence(phrase):
    """
    Check if the phrase starts with a subject or verb, indicating a complete sentence.
    """
    tokens = word_tokenize(phrase)
    pos_tags = pos_tag(tokens)
    
    # print(pos_tags)
    # If the first word is a pronoun (PRP) or a verb (VB, VBD, VBG, etc.), it's likely a sentence.
    if pos_tags:
      # print(pos_tags)
      for idx, pt in enumerate(pos_tags):
       if pt[0] == "for":
        idx += 1
        while idx < len(pos_tags) and is_not_punctuation(pos_tags[idx][1]):
          if pos_tags[idx][1] in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}: 
            return True
          idx += 1
    return False

def strip_punctuation(sentence):
    # Define a regex pattern to match all punctuation marks
    pattern = r'[^\w\s]'
    
    # Replace all punctuation marks with an empty string
    stripped_sentence = re.sub(pattern, '', sentence)

    stripped_sentence = stripped_sentence.strip()
    
    return stripped_sentence
def count_words(sentence):
    # Split the sentence into words based on whitespace and count the number of words
    words = sentence.split()
    return len(words)

def separate_sentences_with_conjunctions(text):
    text = text.lower()
    # Define the list of coordinating conjunctions (case-insensitive)
    conjunction = ['for ', 'and ', 'but ', 'nor ', 'or ', 'so ', 'yet ']
    conjunctions = ['for', 'and', 'but', 'nor', 'or', 'so', 'yet']
    result = []
    # found coordinating conjunctions, special case is 'yet, '
    if any(conj in text for conj in conjunction) and is_complete_sentence(text) and "yet, " not in text:
      pattern = r'[^\w\s]'
      # Replace all punctuation marks with a period
      text = re.sub(pattern, '.', text)
      
      # Tokenize the text into sentences
      sentences = sent_tokenize(text)
        
      # Create a regex pattern to match sentences starting with any conjunction
      pattern = r'^\s*(' + '|'.join(conjunctions) + r')\b'
      
      # Process sentences and filter based on the pattern
     
      for sentence in sentences:
          # Clean up sentence and check if it starts with any of the conjunctions
          cleaned_sentence = sentence.strip()
          if re.match(pattern, cleaned_sentence, re.IGNORECASE):
            # result.append(strip_punctuation(cleaned_sentence))
            result.append(count_words(strip_punctuation(cleaned_sentence)))
          else:
            # result.append(strip_punctuation(sentence))
            result.append(count_words(strip_punctuation(sentence)))
    else:
      # result.append(strip_punctuation(text))
      return count_words(strip_punctuation(text))
    
    return max(result)

max_num_data = []


# Specify the path to your .jsonl file
file_path = '/content/animate_subject_trans.jsonl'


def write_json_lines(filename, data):
    # Write each JSON object as a separate line in a JSON file
    with open(filename, 'w') as file:
      for item in data:
        json.dump(item, file)
        file.write('\n')

# for generating json file output
def main():
    num = 0
    res = []
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line as a JSON object
            data = json.loads(line)
            s1, s2 = data['sentence_good'], data['sentence_bad']
            len1, len2 = separate_sentences_with_conjunctions(s1), separate_sentences_with_conjunctions(s2)
            if len1 < 10 and len2 < 10:
            #and ('if' in s1.split() or 'because' in s1.split() or 'why' in s1.split() or 'if' in s2.split() or 'because' in s2.split() or 'why' in s2.split()): 
            # print(line)
                res.append(data)
                max_num_data.append(len1)
                max_num_data.append(len2)

    write_json_lines("agent-action-object.jsonl", res)
    # print some statistics: size of data and average C-UNIT
    print(len(max_num_data), sum(max_num_data)/ len(max_num_data))


