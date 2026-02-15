daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in range(len(weekdays)):  # atau len(daily_promotions)
    weekday = weekdays[day]
    promotion = daily_promotions[day]
    print(f"{weekday}: Promotion on {promotion}")
