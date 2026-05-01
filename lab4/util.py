def print_header(text: str, length: int = 60) -> None:
    header = f" {text} ".center(length, "=")
    print(header)
