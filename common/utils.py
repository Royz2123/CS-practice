def display_name(name: str) -> str:
    name = name.replace("Exercise", "תרגיל")
    name = name.replace("Chapter", "פרק")
    name = name.replace("_", " ")
    return name
