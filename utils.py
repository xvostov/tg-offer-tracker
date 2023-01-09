def split_list(input_list):
    # Результирующий список
    result_list = []
    # Индекс начала среза
    start_index = 0
    # Индекс конца среза
    end_index = 20
    # Пока end_index меньше длины списка
    while end_index < len(input_list):
        # Добавляем срез списка в результирующий список
        result_list.append(input_list[start_index:end_index])
        # Сдвигаем индексы
        start_index += 20
        end_index += 20

    result_list.append(input_list[start_index:])
    return result_list
