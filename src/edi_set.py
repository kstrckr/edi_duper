
class EdiSet:

    def __init__(self, rows):
        self.edi_names = []
        self.style_names = []

        for row in rows:
            edi_col = row[1]
            style_col = row[5]
            
            if edi_col != "CUSTOMER PROFILE" and len(edi_col) != 0:
                self.edi_names.append(edi_col.replace("\xa0", ""))

            if style_col != "STYLE #" and len(style_col) != 0:
                self.style_names.append(style_col.replace("\xa0", ""))
