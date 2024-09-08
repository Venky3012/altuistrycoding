def max_discount_recursive(tickets: str, k: int) -> str:
    if k == 0:
        return tickets.lstrip('0') or '0'
    
    min_price = tickets
    for i in range(len(tickets)):
     
        new_price = tickets[:i] + tickets[i + 1:]
        min_price = min(min_price, max_discount_recursive(new_price, k - 1))
    
    return min_price

tickets = "203"
k = 2
print(max_discount_recursive(tickets, k))