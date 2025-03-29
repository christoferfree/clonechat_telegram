import time

def get_delays(start_time):
    """
    Retorna os valores de user_delay_seconds, bot_delay_seconds e skip_delay_seconds
    com base no tempo decorrido desde start_time (em segundos).
    """
    # Calcula o tempo decorrido em minutos
    current_time = time.time()
    elapsed_minutes = (current_time - start_time) / 60
    
    # Ciclo completo de 90 minutos
    cycle_time = 90
    elapsed_mod = elapsed_minutes % cycle_time
    
    # Define os valores de delay conforme o intervalo
    if elapsed_mod < 10:
        return 10, 1.2, 1  # 0 a 10 minutos
    elif elapsed_mod < 20:
        return 5, 5, 1     # 10 a 20 minutos
    elif elapsed_mod < 40:
        return 1, 1, 1     # 20 a 40 minutos
    elif elapsed_mod < 45:
        return 10, 1.2, 1  # 40 a 45 minutos
    elif elapsed_mod < 70:
        return 1, 1, 1     # 45 a 70 minutos
    else:
        return 5, 5, 1     # 70 a 90 minutos