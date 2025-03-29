from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


import time
from protect_content.utils.delays import get_delays  # Importa a função criada

# Registra o tempo de início
start_time = time.time()

# Configurações iniciais (exemplo, ajuste conforme o script original)
# Substitua qualquer leitura direta de config.ini por valores dinâmicos
def main():
    # Exemplo de loop principal (simulado)
    while True:
        # Obtém os delays atuais
        user_delay_seconds, bot_delay_seconds, skip_delay_seconds = get_delays(start_time)
        
        print(f"Delays atuais: user={user_delay_seconds}, bot={bot_delay_seconds}, skip={skip_delay_seconds}")
        
        # Use os delays nas operações do script
        time.sleep(user_delay_seconds)  # Exemplo de uso do delay
        
        # Aqui iria o restante da lógica do script (clonagem, etc.)
        # Substitua qualquer uso fixo de delays por essas variáveis dinâmicas

if __name__ == "__main__":
    main()



def save_csv(list_dict: list[dict], path_csv: Path):

    # set_keys = set([key for dict_ in list_dict for key in dict_.keys()])
    dict_default = defaultdict(
        str,
        date="",
        file_size=0,
        type="",
        file_name="",
        caption_sample="",
        id=0,
        duration=0,
        file_path="",
        download=0,
        clone=0,
    )
    for dict_ in list_dict:
        for key in dict_default.keys():
            if key not in dict_:
                dict_[key] = dict_default[key]

    # # Get the list of fields (keys of the dictionaries)
    header = list_dict[0].keys()

    # Open the CSV file for writing
    with open(path_csv, "w", newline="", encoding="utf-8") as csv_file:
        # Create a write object
        reader = csv.DictWriter(csv_file, header)
        # Write the header line with the names of the fields
        reader.writeheader()
        # Write each dictionary as a line in the CSV file
        reader.writerows(list_dict)


def open_csv(path_csv: Path) -> list[dict]:

    # Open the CSV file
    with open(path_csv, "r", encoding="utf-8") as arquivo_csv:
        # Create a reader object
        reader = csv.reader(arquivo_csv)
        # Get the field of fields (first line of the CSV file)
        header = next(reader)
        # Initialize the List of Empty Dictionaries
        data_list_dict = []
        # Item on the remaining lines of the CSV file
        for row in reader:
            # Create a dictionary for the current line with the fields as keys and line values as values
            dict_ = dict(zip(header, row))
            # Add the dictionary to the dictionary list
            data_list_dict.append(dict_)
    return data_list_dict
