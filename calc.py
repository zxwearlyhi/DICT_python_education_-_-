import argparse
import math
import sys

parser = argparse.ArgumentParser(description="Кредитний калькулятор")
parser.add_argument("--type", choices=["diff", "annuity"], help="Тип платежу")
parser.add_argument("--principal", type=float, help="Сума кредиту")
parser.add_argument("--periods", type=int, help="Кількість місяців")
parser.add_argument("--interest", type=float, help="Річна відсоткова ставка")
parser.add_argument("--payment", type=float, help="Щомісячний платіж (для ануїтетних)")

args = parser.parse_args()

# Перевірка валідності параметрів
parameters = [args.type, args.principal, args.periods, args.interest, args.payment]
provided = [p is not None for p in parameters]
count_provided = sum([p is not None for p in [args.principal, args.periods, args.interest, args.payment]])

if args.type not in ['annuity', 'diff'] or args.interest is None:
    print("Incorrect parameters")
    sys.exit()
if any([
    (args.principal is not None and args.principal < 0),
    (args.periods is not None and args.periods < 0),
    (args.payment is not None and args.payment < 0),
    (args.interest is not None and args.interest < 0)
]):
    print("Incorrect parameters")
    sys.exit()


# Диференційований платіж
if args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None or args.payment is not None:
        print("Incorrect parameters")
        sys.exit()
    total = 0
    i = args.interest / (12 * 100)
    for m in range(1, args.periods + 1):
        d = math.ceil(args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods))
        total += d
        print(f"Month {m}: paid out {d}")
    overpay = int(total - args.principal)
    print(f"Overpayment = {overpay}")

# Ануїтетний платіж
elif args.type == "annuity":
    i = args.interest / (12 * 100)
    if args.principal is None:
        annuity = args.payment
        n = args.periods
        P = annuity / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print(f"Your credit principal = {int(P)}!")
        overpay = int(annuity * n - P)
        print(f"Overpayment = {overpay}")

    elif args.payment is None:
        P = args.principal
        n = args.periods
        annuity = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        print(f"Your annuity payment = {math.ceil(annuity)}!")
        overpay = int(math.ceil(annuity) * n - P)
        print(f"Overpayment = {overpay}")

    elif args.periods is None:
        P = args.principal
        annuity = args.payment
        n = math.log(annuity / (annuity - i * P), 1 + i)
        n = math.ceil(n)
        years = n // 12
        months = n % 12
        y_str = f"{years} years" if years else ""
        m_str = f"{months} months" if months else ""
        sep = " and " if years and months else ""
        print(f"You need {y_str}{sep}{m_str} to repay this credit!")
        overpay = int(annuity * n - P)
        print(f"Overpayment = {overpay}")
