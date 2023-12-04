from model.text_classifier import classify

def generate_text(text):
    category = classify(text)
    gen_texts = [{'idx': 1, 'text': text, 'category': category}, {'idx': 2, 'text': text, 'category': category}]
    return gen_texts