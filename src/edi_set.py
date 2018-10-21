import re


class EdiSet:

    def __init__(self, rows):
        self.edi_names = []
        self.style_names = []

        for row in rows:
            edi_col = row[1]
            style_col = row[5]
            
            if edi_col != "CUSTOMER PROFILE" and len(edi_col) != 0:
                edi_name = edi_col.replace("\xa0", "")
                self.edi_names.append(edi_name)

            if style_col != "STYLE #" and len(style_col) != 0:
                output_name = style_col.replace("\xa0", "")
                parsed_output = re.sub(r'\W+', '', output_name).upper()
                self.style_names.append(parsed_output)
