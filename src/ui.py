import os

class UI:

    ask_for_csv_input = '\nPlease drag the CSV file into this window\nor enter X to exit:\n'
    ask_for_photo_dir_input = '\nPlease drag the folder container photos to be renamed:\n'
    preview_header = '\nThe following files will be created'
    creation_confirmation_msg = '\nVerify correct naming and enter [Y/n] to continue '
    process_repeat_msg = '\nContinue with another CSV file? [Y/n]'
    exit_msg = '\nExiting program.'
    invalid_path_msg = 'is not a valid path to an image file, please try again'
    arrow = '--> '
    force_quit = False

    def __init__(self):
            print(self.ask_for_csv_input)
            self.raw_csv_file_path = raw_input(self.arrow)
            self.csv_file_path = self.raw_csv_file_path.strip().strip("'")
            print(self.csv_file_path)

            print(self.ask_for_photo_dir_input)
            self.raw_photo_dir_path = raw_input(self.arrow)
            self.photo_dir_path = self.raw_photo_dir_path.strip().strip("'")
            print(self.photo_dir_path)
            if self.csv_file_path == "X".lower():
                self.force_quit = True

    def print_preview(self, list_of_expected_names):
        print(self.preview_header)
        for name in list_of_expected_names:
            print('--> {}'.format(name))

    def exit_message(self):
        print(self.exit_msg)

    @classmethod
    def clear_screen(self):
        os.system('cls' if os.name=='nt' else 'clear')

    @classmethod
    def path_error_message(self, invalid_path):
        print('"{}" '.format(invalid_path) + self.invalid_path_msg)