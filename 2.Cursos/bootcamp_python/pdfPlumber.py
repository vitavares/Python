# %%
import pdfplumber as pp
import os
# %%
pdf = pp.open('storage/modelo_de_relatorio.pdf')
# %%
page1 = pdf.pages[0]
page2 = pdf.pages[1]
page3 = pdf.pages[2]
# %%
texto_pag_1 = page1.extract_text()