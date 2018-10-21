import os
import shutil

class File_generator:

    file_suffix = "_9"
    

    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.output_dir = os.path.join(target_dir, "output")

        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)

    def create_edi_styles(self, edi_creators):

        for creator in edi_creators:
            for edi_name in creator.edi_names:
                target_file = os.path.join(self.target_dir, edi_name)
                extension = edi_name[-4:]

                if os.path.isfile(target_file):
                    for output_name in creator.style_names:
                        output_name += self.file_suffix
                        output_name += extension
                        output_file = os.path.join(self.output_dir, output_name)
                        shutil.copy(target_file, output_file)