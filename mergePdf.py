from PyPDF2 import PdfFileMerger

pdfs =[] 
for i in range(315):
    pdfs.append('page'+str(i)+'.pdf')
merger = PdfFileMerger()
print(pdfs)
for pdf in pdfs:
    merger.append(open(pdf,'rb'))
with open("result.pdf", "wb") as fout:
    merger.write(fout)
