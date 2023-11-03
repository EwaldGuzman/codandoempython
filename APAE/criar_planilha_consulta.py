from openpyxl import load_workbook, Workbook
from pathlib import Path
import os
from tkinter import filedialog
class Planilha:

    def __init__(self, user):

        self.plan = Path(fr'Tabelas_xlsx/Cadastros_xlsx/{user}.xlsx').absolute()

        self.criar()

    def criar(self):

        if self.plan.exists():
            pass
        else:
            print('Não existe')
            doc = Workbook(self.plan)

            # plan = doc.active
            # plan['a1'] = "DATA CONSULTA"
            # plan['B1'] = "SUS"
            # plan['C1'] = "PACIENTE"
            # plan['D1'] = "NASCIMENTO"
            # plan['E1'] = "IDADE"
            # plan['F1'] = "TELEFONE"
            # plan['G1'] = "RUA"
            # plan['H1'] = "NUMERO"
            # plan['I1'] = "BAIRRO"
            # plan['J1'] = "CIDADE"
            # plan['K1'] = "CEP"
            # plan['L1'] = "DESCRIÇÃO"
            doc.save(self.plan)




Planilha('lucas')
