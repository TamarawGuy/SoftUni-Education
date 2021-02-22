book_pages = int(input())
pages_for_1_hour = int(input())
days_to_complete_book = int(input())

total_time = book_pages / pages_for_1_hour
hours_per_day = total_time / days_to_complete_book
print(hours_per_day)