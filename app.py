
from model.sentiment_model import analyze_sentiment
from utils.preprocess import clean_text

def main():
    print("🤖 AI Sentiment Analyzer")
    print("Type 'exit' to quit\n")

    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            print("Goodbye 👋")
            break

        cleaned = clean_text(text)
        sentiment, confidence = analyze_sentiment(cleaned)

        print(f"\nSentiment: {sentiment}")
        print(f"Confidence: {round(confidence, 2)}\n")


if __name__ == "__main__":
    main()
