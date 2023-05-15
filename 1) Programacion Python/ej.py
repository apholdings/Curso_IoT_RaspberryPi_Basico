try:
    # lanzamos un error con un mensaje personalizado
    raise ValueError("Este es un error personalizado.")
except ValueError as e:
    print(f"Error: {e}")
