from __future__ import annotations

import asyncio
import multiprocessing


import time
from utils.delays import get_delays  # Importa a função criada

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



def func_subprocess(func_, dict_params: dict, pipe):

    result = asyncio.run(func_(**dict_params))
    pipe.send(result)


def time_out(
    sec_time_out: int, func_, dict_params: dict = {}, restart: bool = True
):
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(
        target=func_subprocess, args=[func_, dict_params, child_conn]
    )
    p.start()

    p.join(sec_time_out)

    if p.is_alive():
        p.terminate()
        if restart:
            print("\nTook too long. Restarting.")
            return time_out(sec_time_out, func_, dict_params, restart)
    else:
        return parent_conn.recv()
