import requests
file_url = "https://survya.com/resume/Survya_Singh_CV.pdf"
 
r = requests.get(file_url, stream = True)
 
with open("python.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
 
         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk)