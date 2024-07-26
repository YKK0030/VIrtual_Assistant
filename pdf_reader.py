import pdfplumber
import speak
from transformers import pipeline

def summarize_text(text):
    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"An error occurred during summarization: {str(e)}"
        
        
def pdf_reader(file_path):
    try:
        with pdfplumber.open(file_path) as book:
            pages = len(book.pages)
            speak.speak(f"Total number of pages in this book: {pages}")

            speak.speak("Sir, please enter the page number I have to read.")
            while True:
                try:
                    pg = int(input("Please enter the page number: "))
                    if pg < 0 or pg >= pages:
                        speak.speak(f"Invalid page number. Please enter a number between 0 and {pages - 1}.")
                        continue
                    break
                except ValueError:
                    speak.speak("Invalid input. Please enter a valid page number.")

            page = book.pages[pg]
            text = page.extract_text()

            if text.strip():
                speak.speak(text)
            else:
                speak.speak("The page is empty or could not be read.")

    except FileNotFoundError:
        speak.speak("The specified file was not found. Please check the file name and path.")

    except Exception as e:
        speak.speak(f"An error occurred while reading the PDF: {str(e)}")

if __name__ == '__main__':
    pdf_reader("/home/yadnitkale/Downloads/WAD (1).pdf")
