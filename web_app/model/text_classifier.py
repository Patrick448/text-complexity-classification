
import pickle
import sys


def classify(input_text):
    model = None
    count_vect = None
    tfidf_transformer = None

    with open('web_app/model/text_classifier', 'rb') as training_model:
        model = pickle.load(training_model)

    with open('web_app/model/count_vect', 'rb') as count_vect_file:
        count_vect = pickle.load(count_vect_file)

    with open('web_app/model/tfidf_transformer', 'rb') as tfidf_transformer_file:
        tfidf_transformer = pickle.load(tfidf_transformer_file)

    # create bag of words representation for test set
    input_text_counts = count_vect.transform([input_text])
    input_text_tfidf = tfidf_transformer.transform(input_text_counts)
    category_map = {0: "Ensino Fundamental I",
                    1: "Ensino Fundamental II",
                    2: "Ensino Médio",
                    3: "Ensino Superior"}

    prediction = model.predict(input_text_tfidf)
    return category_map[prediction[0]]


def read_file(file_path):
    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
        return input_text

def main():
    print(sys.argv)

    if sys.argv[1] == "loop":
        while True:
            file_path = input("Enter file path: ")
            text = read_file(file_path)
            print(classify(text))

    elif sys.argv[1] == "once":
        file_path = sys.argv[2]
        text = read_file(file_path)
        print(classify(text))


if __name__ == '__main__':
    main()

