import pdfplumber

# ctrl + shift + P    >    select interpreter     >  python 버전 세팅

pdf = pdfplumber.open("아뱅.pdf")
num = len(pdf.pages)

for i in range(num):
     print(pdf.pages[i].extract_text())

# import googletrans
# from googletrans import Translator
 
# print(googletrans.LANGUAGES)
# translator = Translator() 

# text1 = "안녕하세요"
# for i in googletrans.LANGUAGES:
#     trans1 = translator.translate(text1, src='ko', dest=i)
#     print(f"{googletrans.LANGUAGES[i]}: ", trans1.text)
