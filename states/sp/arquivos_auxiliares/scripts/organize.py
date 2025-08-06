import os
import shutil

# organizing files from datasus
# orginal_path: path to the directory where the files are located
# state: two-letter abbreviation of the state (e.g., 'sp' for São Paulo
def organize_files(original_path:str, state:str, start_year: 8, end_year: int = 25):
    print('')
    print(original_path)
    print('')
    state = state.upper()
    file_structure = 'AR' + state
    type = '.dbc'

    # creating list with years
    years = []
    for y in range(start_year, end_year):
        if y < 10:
            years.append('0' + str(y))
        else:
            years.append(str(y))
    # creating list with months
    months = []
    for m in range(1,13):
        if m < 10:
            months.append('0' + str(m))
        else:
            months.append(str(m))

    # creating directory for each year
    for y in years:
        path = os.path.join(original_path, y)        
        # creating directory if it does not exist
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {y}")
        else:
            print(f"Directory already exists: {y}")

    # checking for files and moving them to the corresponding directory
    for y in years:
        path = os.path.join(original_path, y)
        # creating directory for each month
        for m in months:
            file_name = f"{file_structure}{y}{m}{type}"
            file_name = os.path.join(original_path, file_name)
            print(f"Checking for file: {file_name}")                        
            # moving file to the corresponding directory
            if os.path.exists(file_name):
                print(f"File found: {file_name}")                     
                shutil.move(file_name, path)                
                print(f"Moved {file_name} to {y}/")

organize_files('C:\\Users\\175 MX\\Documents\\Gustavo\\datasus\\data_rt_states\\states\\sc', 'sc', 8, 25)