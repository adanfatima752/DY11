def safe_convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None
