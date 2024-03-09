# Імпортування необхідних бібліотек для експерименту
import pandas as pd
import timeit

# Визначення сум, які будуть тестуватися
amounts = [13, 113, 1133]

# Списки для зберігання часу виконання для кожної суми
greedy_times = []
dynamic_times = []

# Визначення функції жадібного алгоритму
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Обчислення кількості монет даного номіналу
            amount -= coin * count  # Зменшення залишкової суми
            result[coin] = count  # Збереження результату
            if amount == 0:  # Якщо залишкова сума дорівнює нулю, завершення роботи
                break
    return result

# Визначення функції динамічного програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)  # Ініціалізація масиву з нескінченностями
    dp[0] = 0  # Базовий випадок: мінімальна кількість монет для суми 0
    coin_used = {0: []}  # Зберігання використаних монет для кожної суми
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1  # Оновлення мінімальної кількості монет
                coin_used[i] = coin_used[i - coin] + [coin]  # Зберігання шляху використання монет
    
    # Формування словника з результатами
    return {coin: coin_used[amount].count(coin) for coin in coin_used[amount]}

# Цикл для вимірювання часу виконання та виведення результатів розбиття суми на монети
for amount in amounts:
    # Вимірювання часу виконання жадібного алгоритму
    greedy_time = timeit.timeit('find_coins_greedy({})'.format(amount), globals=globals(), number=1000)
    greedy_times.append(greedy_time)
    
    # Вимірювання часу виконання алгоритму динамічного програмування
    dynamic_time = timeit.timeit('find_min_coins({})'.format(amount), globals=globals(), number=1000)
    dynamic_times.append(dynamic_time)

    # Виведення на екран словника з кількістю монет
    print(f"Для суми: {amount}")
    print("Жадібний алгоритм:", find_coins_greedy(amount))
    print("Динамічне програмування:", find_min_coins(amount))
    print()  # Для кращої читабельності результатів

# Створення DataFrame для відображення результатів
results_df = pd.DataFrame({
    'Amount': amounts,
    'Greedy Algorithm Time (s)': greedy_times,
    'Dynamic Programming Time (s)': dynamic_times
})

# Виведення таблиці результатів
print(results_df)