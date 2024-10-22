import csv
import json

# Чтение visit_log.csv и создание словаря с user_id и источниками
visit_dict = {}
with open('visit_log.csv', 'r', encoding='utf-8') as visit_file:
    visit_reader = csv.reader(visit_file)
    for row in visit_reader:
        user_id, source = row
        visit_dict[user_id] = source

# Создание funnel.csv и запись данных
with open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:
    funnel_writer = csv.writer(funnel_file)
    funnel_writer.writerow(['user_id', 'source', 'category'])  # Запись заголовков

    # Чтение purchase_log.csv и сопоставление с visit_log
    with open('purchase_log.csv', 'r', encoding='utf-8') as purchase_file:
        for line in purchase_file:
            purchase_data = json.loads(line)
            user_id = purchase_data['user_id']
            category = purchase_data['category']
            if user_id in visit_dict:
                source = visit_dict[user_id]
                # Запись строки в funnel.csv
                funnel_writer.writerow([user_id, source, category])