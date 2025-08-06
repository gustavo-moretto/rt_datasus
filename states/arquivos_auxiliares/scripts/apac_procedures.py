import pandas as pd

def old_apacs():
    """
    This function is used to extract the APAC procedure codes from the PRT 263/2019 regulation in Brazil.
    It reads the HTML page, extracts the first table, cleans the 'CÓDIGO' column, and converts it into a dictionary.
    """
    
    # Here we are going to extract the procedure codes from PRT 263/2019, which is the regulation for APACs in Brazil
    url = 'https://bvsms.saude.gov.br/bvs/saudelegis/sas/2019/prt0263_27_02_2019.html'

    # Extract all tables from the HTML page
    tables = pd.read_html(url, encoding='latin1', header=0)

    # Get the first table
    first_table = tables[0]

    # Remove dots and dashes from 'CÓDIGO' column
    first_table['CÓDIGO'] = first_table['CÓDIGO'].str.replace('.', '', regex=False).str.replace('-', '', regex=False)


    # Transforming table in a dictionary
    dict_procedures = first_table.set_index('CÓDIGO').to_dict()

    return dict_procedures



# Here we are going to extract the procedure codes from PRT 263/2019, which is the regulation for APACs in Brazil
url = 'https://bvsms.saude.gov.br/bvs/saudelegis/sas/2019/prt0263_27_02_2019.html'

# Extract all tables from the HTML page
tables = pd.read_html(url, encoding='latin1', header=0)

# Interact between tables
first_table = tables[5]['Procedimento']

print(first_table.to_dict())