import sqlite3
import random

DB_NAME = 'banking_system.db'
IIN = '400000'  # Ідентифікатор емітента (Issuer Identification Number)

def luhn_checksum(card_num: str) -> int:
    """
    Обчислює контрольну цифру за алгоритмом Луна для заданого номера картки (без контрольної цифри).
    """
    digits = [int(d) for d in card_num]
    # Подвоєння кожної другої цифри, рахуючи зліва з індексу 0
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return (sum(digits) * 9) % 10

def generate_card_number(account_id: int) -> str:
    """
    Генерує номер картки відповідно до алгоритму Луна.
    """
    account_id_str = f"{account_id:09d}"  # 9-значний account id
    partial_number = IIN + account_id_str
    checksum = luhn_checksum(partial_number)
    return partial_number + str(checksum)

def validate_card_number(card_num: str) -> bool:
    """
    Перевіряє номер картки на валідність за алгоритмом Луна.
    """
    if not card_num.isdigit() or len(card_num) != 16:
        return False
    nums = [int(ch) for ch in card_num[:-1]]
    checksum = luhn_checksum(card_num[:-1])
    return int(card_num[-1]) == checksum

def validate_pin(pin: str) -> bool:
    """
    Перевіряє, що PIN складається з 4 цифр.
    """
    return pin.isdigit() and len(pin) == 4

class BankingDB:
    def __init__(self, db_file=DB_NAME):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        """
        Створює таблицю accounts, якщо вона ще не існує.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_number TEXT UNIQUE,
                pin TEXT,
                balance INTEGER DEFAULT 0
            );
        ''')
        self.conn.commit()

    def create_account(self, pin: str) -> dict:
        """
        Створює новий акаунт з унікальним номером картки і PIN.
        """
        cursor = self.conn.cursor()
        while True:
            # Кілька спроб для генерації унікального номера картки
            account_id = random.randint(0, 999_999_999)
            card_number = generate_card_number(account_id)
            cursor.execute('SELECT 1 FROM accounts WHERE card_number=?', (card_number,))
            if not cursor.fetchone():
                break
        cursor.execute('''
            INSERT INTO accounts(card_number, pin, balance) VALUES (?, ?, 0)
        ''', (card_number, pin))
        self.conn.commit()
        return {'card_number': card_number, 'pin': pin, 'balance': 0}

    def get_account(self, card_number: str, pin: str) -> dict or None:
        """
        Отримати акаунт за номером картки та піном.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT card_number, pin, balance FROM accounts WHERE card_number=? AND pin=?
        ''', (card_number, pin))
        row = cursor.fetchone()
        if row:
            return {'card_number': row[0], 'pin': row[1], 'balance': row[2]}
        return None

    def get_account_by_number(self, card_number: str) -> dict or None:
        cursor = self.conn.cursor()
        cursor.execute('SELECT card_number, pin, balance FROM accounts WHERE card_number=?', (card_number,))
        row = cursor.fetchone()
        if row:
            return {'card_number': row[0], 'pin': row[1], 'balance': row[2]}
        return None

    def update_balance(self, card_number: str, amount: int):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE card_number=?', (amount, card_number))
        self.conn.commit()

    def delete_account(self, card_number: str):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM accounts WHERE card_number=?', (card_number,))
        self.conn.commit()

    def close(self):
        self.conn.close()

def input_pin():
    """
    Запитує у користувача PIN, перевіряючи коректність вводу.
    """
    while True:
        pin = input('Введіть PIN (4 цифри): ')
        if validate_pin(pin):
            return pin
        print('Некоректний формат PIN. Спробуйте ще раз.')

def input_card_number():
    """
    Запитує у користувача номер картки, перевіряючи коректність вводу.
    """
    while True:
        card_num = input('Введіть номер картки (16 цифр): ')
        if validate_card_number(card_num):
            return card_num
        print('Некоректний номер або номер не проходить перевірку Луна. Спробуйте ще раз.')

def input_amount():
    """
    Запитує у користувача суму операції (ціле позитивне число).
    """
    while True:
        try:
            amount = int(input('Введіть суму: '))
            if amount > 0:
                return amount
            else:
                print('Сума має бути більше нуля!')
        except ValueError:
            print('Сума повинна бути цілим числом!')

def main_menu():
    print("\n=== Банківська система ===")
    print("1. Створити акаунт")
    print("2. Увійти до акаунта")
    print("0. Вийти")

def account_menu():
    print("\n=== Меню акаунта ===")
    print("1. Переглянути баланс")
    print("2. Поповнити рахунок")
    print("3. Переказ на іншу картку")
    print("4. Закрити акаунт")
    print("5. Вийти")

def main():
    db = BankingDB()
    try:
        while True:
            main_menu()
            choice = input("Виберіть дію: ")
            if choice == '1':
                # Створення акаунта
                pin = input_pin()
                acc = db.create_account(pin)
                print('\nАкаунт створено! Ваші дані:')
                print('Номер картки:', acc['card_number'])
                print('PIN:', acc['pin'])
            elif choice == '2':
                card_number = input('Введіть номер картки: ')
                pin = input('Введіть PIN: ')
                acc = db.get_account(card_number, pin)
                if acc:
                    print('\nВхід виконано успішно!')
                    # Дії в акаунті
                    while True:
                        account_menu()
                        act = input('Виберіть дію: ')
                        if act == '1':
                            print(f"Поточний баланс: {db.get_account_by_number(card_number)['balance']} грн")
                        elif act == '2':
                            amount = input_amount()
                            db.update_balance(card_number, amount)
                            print('Рахунок поповнено.')
                        elif act == '3':
                            print("=== Переказ коштів ===")
                            dst_card = input('Введіть номер картки отримувача: ')
                            if dst_card == card_number:
                                print("Неможливо переказати на власну картку.")
                                continue
                            if not validate_card_number(dst_card):
                                print("Некоректний номер картки!")
                                continue
                            dst_acc = db.get_account_by_number(dst_card)
                            if not dst_acc:
                                print("Картку не знайдено в системі!")
                                continue
                            amount = input_amount()
                            src_balance = db.get_account_by_number(card_number)['balance']
                            if amount > src_balance:
                                print("Недостатньо коштів!")
                                continue
                            db.update_balance(card_number, -amount)
                            db.update_balance(dst_card, amount)
                            print("Операція виконана успішно.")
                        elif act == '4':
                            db.delete_account(card_number)
                            print("Акаунт закрито!")
                            break
                        elif act == '5':
                            print("Ви вийшли з акаунта.")
                            break
                        else:
                            print("Некоректний вибір. Спробуйте ще раз.")
                else:
                    print("Невірний номер картки або PIN.")
            elif choice == '0':
                print("Дякуємо за використання банківської системи!")
                break
            else:
                print("Некоректний вибір. Спробуйте ще раз.")
    finally:
        db.close()

if __name__ == '__main__':
    main()
