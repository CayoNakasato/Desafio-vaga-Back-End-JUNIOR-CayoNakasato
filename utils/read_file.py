def read_txt(path):
    separated_info = []

    with open(path, "r", encoding="utf8") as file:
        for info in file:
            separated_info.append(info)
            
        return separated_info

def split_transactions(transaction):
    
    type = transaction[0:1]

    date = transaction[1:9]

    value = transaction[9:19]

    cpf = transaction[19:30]

    card = transaction[30:42]

    time = transaction[42:48]

    owner = transaction[48:62]

    shop_name = transaction[62:79]

    year = date[0:4]

    month = date[4:6]

    day = date[6:8]

    realDate = f"{year}/{month}/{day}"

    hour = time[0:2]

    minutes = time[2:4]

    seconds = time[4:6]

    realHour = f"{hour}:{minutes}:{seconds}"

    value = (int(value)/100)

    transaction_info = {
        "type": type,
        "date": realDate,
        "value": value,
        "cpf": cpf,
        "card": card,
        "hour": realHour,
        "owner": owner.rstrip(),
        "shop_name": shop_name.rstrip(),
    }

    return transaction_info

def transaction_list(path):
    cnab_file = read_txt(path)
    
    transaction_list = []

    for file in cnab_file:
        transaction = split_transactions(file)
        transaction_list.append(transaction)

    return transaction_list

def sum_values(transaction_list):
    sum = 0
    for transaction in transaction_list:
        if transaction["type"] == "2" or transaction["type"] == "3" or transaction["type"] == "9":
            sum -= transaction["value"]
        else:
          sum += transaction["value"]
    return sum
