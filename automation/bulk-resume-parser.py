import re,pandas,os,pdfminer,spacy
import pdf2txt

def convertPdf(f):
    output_filename = os.path.basename(os.path.splitext(f)[0]) + '.txt'
    output_filepath = os.path.join("output/txt/", output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath])
    print(output_filepath + "saved seccesfully")
    return open(output_filepath).read()

nlp = spacy.load('en_core_web_sm')

resultDict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []

def parse_content(text):
    skillset = re.compile("python|java|sql|hadoop|tableau")
    phone_num= re.compile(
        "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    )

    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ is "PERSON"][0]
    print(name)
    email = [word for word in doc if word.like_email == True][0]
    print(email)
    
    phone = str(re.findall(phone_num, text.lower()))
    skills_list = re.findall(skillset, text.lower())
    unique_skills_list = str(set(skills_list))

    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("extraction copleted successfully!!")

for file in os.listdir("resumes/"):
    if file.endswith(".pdf"):
        print(f"Reading...........{file}")
        txt = convertPdf(os.path.join('resumes/',file))
        parse_content(txt)

resultDict["name"] = names
resultDict["phone"] = phones
resultDict["email"] = emails
resultDict["skills"] = skills

resltDf = pandas.DataFrame(resultDict)
resltDf.to_csv('filedir/desiredfile/filename')