import random

def generate_domino_set():
    dominoes = []
    for i in range(7):
        for j in range(i, 7):
            dominoes.append([i, j])
    random.shuffle(dominoes)
    return dominoes

def distribute_pieces(dominoes):
    user = []
    computer = []
    for _ in range(7):
        user.append(dominoes.pop())
        computer.append(dominoes.pop())
    return user, computer, dominoes

# Старт гри
dominoes = generate_domino_set()
user_pieces, computer_pieces, stock = distribute_pieces(dominoes)
snake = []
status = "user"  # або "computer"

def find_start_piece(user, computer):
    for i in range(6, -1, -1):
        piece = [i, i]
        if piece in user:
            user.remove(piece)
            return 'user', piece
        elif piece in computer:
            computer.remove(piece)
            return 'computer', piece
    return None, None

status, start_piece = find_start_piece(user_pieces, computer_pieces)
if start_piece:
    snake.append(start_piece)
else:
    print("Помилка: Не знайдено стартову кісточку!")
    exit()

def print_state(stock, comp, snake, user):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(comp)}")
    if len(snake) > 6:
        print(f"{snake[:3]}...{snake[-3:]}")
    else:
        print(snake)
    print("\nYour pieces:")
    for idx, piece in enumerate(user, 1):
        print(f"{idx}:{piece}")

def user_move(user, snake, stock):
    while True:
        choice = input("Ваш хід. Введіть номер кісточки, яку бажаєте покласти (від'ємне - ліворуч, додатне - праворуч). 0 - взяти з резерву: ")
        if not choice.lstrip('-').isdigit():
            print("Помилка: введіть число!")
            continue
        choice = int(choice)
        if choice == 0:
            if stock:
                user.append(stock.pop())
                print("Взяли кісточку з резерву.")
                return
            else:
                print("Резерв порожній. Пропускаєте хід.")
                return
        if abs(choice) > len(user):
            print("Немає такої кісточки!")
            continue
        idx = abs(choice) - 1
        piece = user[idx]
        left_val = snake[0][0]
        right_val = snake[-1][1]
        if choice > 0:
            # Додати праворуч
            if right_val in piece:
                if piece[0] == right_val:
                    snake.append(piece)
                else:
                    snake.append(piece[::-1])
                user.pop(idx)
                return
            else:
                print("Ця кісточка не підходить праворуч.")
        else:
            # Додати ліворуч
            if left_val in piece:
                if piece[1] == left_val:
                    snake.insert(0, piece)
                else:
                    snake.insert(0, piece[::-1])
                user.pop(idx)
                return
            else:
                print("Ця кісточка не підходить ліворуч.")

def computer_move(comp, snake, stock):
    possible_moves = []
    left_val = snake[0][0]
    right_val = snake[-1][1]
    for idx, piece in enumerate(comp):
        if left_val in piece or right_val in piece:
            possible_moves.append((idx, piece))
    if possible_moves:
        idx, piece = possible_moves[0]
        # Простий вибір: перший доступний хід
        if piece[0] == right_val or piece[1] == right_val:
            if piece[0] == right_val:
                snake.append(piece)
            else:
                snake.append(piece[::-1])
        else:
            # left
            if piece[1] == left_val:
                snake.insert(0, piece)
            else:
                snake.insert(0, piece[::-1])
        comp.pop(idx)
    else:
        if stock:
            comp.append(stock.pop())
        # Якщо резерв порожній – пропускаємо хід.

def is_game_over(user, comp, stock, snake):
    # Перемога одного з гравців
    if not user:
        print("Ви виграли!")
        return True
    if not comp:
        print("Комп'ютер виграв!")
        return True
    # Нічия: перевірка на блокування
    left = snake[0][0]
    right = snake[-1][1]
    if left == right and sum(1 for p in snake if left in p) == 8:
        print("Нічия!")
        return True
    return False

# Основний ігровий цикл
while True:
    print_state(stock, computer_pieces, snake, user_pieces)
    if is_game_over(user_pieces, computer_pieces, stock, snake):
        break
    if status == "user":
        user_move(user_pieces, snake, stock)
        status = "computer"
    else:
        input("Computer is about to make a move. Press Enter to continue...")
        computer_move(computer_pieces, snake, stock)
        status = "user"

