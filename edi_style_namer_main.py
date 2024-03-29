#!/usr/bin/python

from src import ui
from src import csv_splitter
from src import edi_set
from src import file_generator

if __name__ == '__main__':

    repeating = True
    retry = False
    incorrect_path = None

    while repeating:
        ui.UI.clear_screen()

        if retry:
            ui.UI.path_error_message(incorrect_path)

        current_ui = ui.UI()
        if current_ui.force_quit == True:
            current_ui.exit_message()
            break

        try:
            retry = False
            incorrect_path = None
            raw_split_csv = csv_splitter.CsvSplitter.split_csv(current_ui.csv_file_path)

            edi_creators = []

            for batch in raw_split_csv:
                edi_batch = edi_set.EdiSet(batch)
                if len(edi_batch.edi_names) > 0:
                    edi_creators.append(edi_batch)
            
            for creator in edi_creators:
                value = creator.edi_names
                key = creator.style_names
                print(value, key)

            fg = file_generator.File_generator(current_ui.photo_dir_path)

            fg.create_edi_styles(edi_creators)

            #ui.UI.clear_screen()

            repeating = False

        except ValueError:
            incorrect_path = current_ui.csv_file_path
            retry = True