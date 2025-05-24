def print_help():
    print("Available formatters: plain bold italic header link inline-code unordered-list ordered-list new-line")
    print("Special commands: !help !done")

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_inline_code(text):
    return f"`{text}`"

def format_link(label, url):
    return f"[{label}]({url})"

def format_header(level, text):
    return f"{'#' * level} {text}\n"

def format_unordered_list(rows):
    return ''.join([f"* {item}\n" for item in rows])

def format_ordered_list(rows):
    return ''.join([f"{i+1}. {item}\n" for i, item in enumerate(rows)])

formatters = {
    "plain": format_plain,
    "bold": format_bold,
    "italic": format_italic,
    "inline-code": format_inline_code,
    "link": format_link,
    "header": format_header,
    "unordered-list": format_unordered_list,
    "ordered-list": format_ordered_list,
    "new-line": lambda: "\n",
}

result = ""
while True:
    cmd = input("Choose a formatter: ")
    if cmd == "!help":
        print_help()
        continue
    if cmd == "!done":
        print(result)
        break
    if cmd not in formatters:
        print("Unknown formatting type or command")
        continue

    if cmd == "header":
        while True:
            try:
                level = int(input("Level: "))
                if not (1 <= level <= 6):
                    print("The level should be within the range of 1 to 6")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")
        text = input("Text: ")
        result += format_header(level, text)
    elif cmd in ["plain", "bold", "italic", "inline-code"]:
        text = input("Text: ")
        result += formatters[cmd](text)
    elif cmd == "link":
        label = input("Label: ")
        url = input("URL: ")
        result += format_link(label, url)
    elif cmd in ["ordered-list", "unordered-list"]:
        while True:
            try:
                rows_count = int(input("Number of rows: "))
                if rows_count <= 0:
                    print("The number of rows should be greater than zero")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")
        rows = []
        for i in range(rows_count):
            row = input(f"Row #{i+1}: ")
            rows.append(row)
        result += formatters[cmd](rows)
    elif cmd == "new-line":
        result += "\n"

    print(result)
