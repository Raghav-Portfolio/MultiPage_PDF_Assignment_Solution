import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path

pdf=FPDF(orientation = 'P', unit='mm', format='A4')

filepaths=glob.glob('Text+Files/*.txt')

for filepath in filepaths:
    pdf.add_page()
   
    header_name = filepath.split('\\')[1].split('.')[0].capitalize()
    pdf.set_font(family='Times', style='B', size=22)
    pdf.cell(w=0, h=12, txt = header_name, align ='L', ln=1)
    
    pdf.ln(5)
    with open(filepath,'r') as f:
        m=f.read()
    pdf.set_font(family='Times', size=8)
    pdf.multi_cell(w=0, h=6, txt=m)
    

pdf.output('solution.pdf')