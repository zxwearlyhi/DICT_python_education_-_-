import requests

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Будь ласка, введіть додатнє число.")
                continue
            return value
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")

def get_currency_input(prompt, available_currencies):
    while True:
        currency = input(prompt).lower()
        if currency not in available_currencies:
            print(f"Невідома валюта. Оберіть одну з: {', '.join(available_currencies)}.")
        else:
            return currency

# Етап 1: простий конвертер у долари
print("Етап 1: Конвертація mycoin у долари (USD)")
mycoins = get_float_input("Введіть кількість mycoin: ")
rate = get_float_input("Введіть курс обміну (скільки доларів за один mycoin): ")
usd_amount = mycoins * rate
print(f"Сума у доларах: {usd_amount:.2f}")
print("="*40)

# Етап 2: конвертація у декілька валют
print("Етап 2: Конвертація mycoin в інші валюти")
rates = {
    "ars": 0.82,      # аргентинське песо
    "hnl": 0.17,      # гондураська лемпіра
    "aud": 1.9622,    # австралійський долар
    "mad": 0.208      # марокканський дирхам
}
for cur, cur_rate in rates.items():
    print(f"1 mycoin = {cur_rate} {cur.upper()}")

currency = get_currency_input("Оберіть валюту для конвертації (ars, hnl, aud, mad): ", list(rates.keys()))
coins = get_float_input("Введіть кількість mycoin для конвертації: ")
converted = coins * rates[currency]
print(f"{coins} mycoin = {converted:.2f} {currency.upper()}")
print("="*40)

# Етап 3: конвертація через API у долари та євро
print("Етап 3: Онлайн конвертація")
BASE_CURRENCY = "usd"
try:
    resp = requests.get(f"http://www.floatrates.com/daily/{BASE_CURRENCY}.json")
    resp.raise_for_status()
    data = resp.json()
    usd_rate = 1.0  # Базова валюта
    eur_rate = data["eur"]["rate"]
    print(f"Курс долара: 1 USD = {usd_rate} USD")
    print(f"Курс євро: 1 USD = {eur_rate} EUR")
except Exception as e:
    print("Не вдалося отримати актуальні курси:", e)
print("="*40)

# Етап 4: Кешування, вибір валюти
print("Етап 4: Конвертер з кешуванням")

cache = {}
base_currency = input("Введіть назву валюти, яку ви хочете обміняти (наприклад, usd): ").lower()
while True:
    target_currency = input("Введіть валюту, у яку хочете обміняти (наприклад, eur, ars, aud): ").lower()
    amount = get_float_input("Введіть суму для обміну: ")

    if target_currency == base_currency:
        print(f"Сума не змінилася: {amount:.2f} {base_currency.upper()}")
        continue

    key = (base_currency, target_currency)
    if key in cache:
        rate = cache[key]
        print("Використовується кешований курс.")
    else:
        try:
            resp = requests.get(f"http://www.floatrates.com/daily/{base_currency}.json")
            resp.raise_for_status()
            data = resp.json()
            if target_currency in data:
                rate = data[target_currency]["rate"]
                cache[key] = rate
                print(f"Отримано курс з API: 1 {base_currency.upper()} = {rate} {target_currency.upper()}")
            else:
                print("Даних по цій валютній парі не знайдено.")
                continue
        except Exception as e:
            print("Не вдалося отримати актуальні курси:", e)
            continue
    result = amount * rate
    print(f"{amount:.2f} {base_currency.upper()} = {result:.2f} {target_currency.upper()}")

    again = input("Бажаєте ще раз? (y/n): ").strip().lower()
    if again != 'y':
        break
