import os
import re
import win32com.client as wc
import docx

def doc2docx(doc_path):
    w=wc.Dispatch('Word.Application')
    w.Visible =0
    w.DisplayAlerts =0
    doc=w.Documents.Open(doc_path)
    docx_path=re.sub('.doc','',doc_path)+'.docx'
    doc.SaveAs(docx_path, 12, False, "", True, "", False, False, False, False)
    doc.Close()
    w.Quit()
    return docx_path

def docx2txt(docx_path):
    content=[]
    doc=docx.Document(docx_path)
    for paragragh in doc.paragraphs:
        content.append(paragragh.text)
    content=" ".join(content)
    txt_path=re.sub('.docx','',docx_path)+'.txt'
    with open(txt_path,'w',encoding='gbk',errors='ignore') as f:
        f.write(content)

if __name__=='__main__':
    ##path='E:\PycharmProjects\文本相似度\\20191205164106\\'
    path = 'E:\PycharmProjects\文本相似度\\20191205164124\\'
    filenames = os.listdir(path)
    pattern = re.compile(r'.*\.doc$')
    for filename in filenames:
        filename = path + filename
        if (pattern.match(filename)):
            filename = doc2docx(filename)
        docx2txt(filename)






