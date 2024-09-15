from transformers import pipeline

def eval():
    generator = pipeline('text-generation', model="facebook/opt-350m")
    print(generator("What are we having for dinner?"))
