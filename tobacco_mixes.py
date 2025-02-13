# Task:
# From tobacco.txt get list of dicts with all tobacco data
# Get mix with two flawors
# Make another dict with random rate of this mix
# Save info about mix to json file

# ==========================DECOMPOSITION==========================
# 1. Read file line by line
# 2. Split line from file by "," separator
# 3. Write splitted data to dict
# 4. Save dict into list
# 5. Get combination of two random list elements
# 6. Save combination into another dict
# 7. Add rating to combination
# 8. Save all of this as json
# 9. Create message with mix


# ==========================ZADANIE==========================
# 1. Добавить возможность делать миксы более чем из 2-х ингридиентов
# 2. Добавить возможность запрашивать вкусы в миксе
# 3. Не смешивать одинаковые вкусы
# 4. Избавиться от дублирования видов чаш в сообщении
# Пример:
# Табак 1 - тяжелая, табак 2 - средняя, табак 3 - тяжелая
# В сообщении "используйте чашу средняя или тяжелая"
import random
import json


def generate_report(tobacco_mix):
    # return f"Чтобы сделать этот крутой микс, возьмите 40% табака {tobacco_mix[0]['tobacco_brand']} со вкусом {tobacco_mix[0]['tobacco_flavor']}, добавьте 50% табака {tobacco_mix[1]['tobacco_brand']} со вкусом {tobacco_mix[1]['tobacco_flavor']} и 10% табака {tobacco_mix[2]['tobacco_brand']} со вкусом {tobacco_mix[2]['tobacco_flavor']}, используйте чашу {tobacco_mix[0]['tobacco_pot']} или {tobacco_mix[1]['tobacco_pot']}"
    # обойти список tobacco_mix['ingridients'] и достать брэнд и вкус (смотри выше)
    # из этого же списка нужно получить список чаш
    # нужно оставить только уникальные чаши
    report = "Чтобы сделать этот крутой микс, возьмите " 
    pot = []
    for ingridient in tobacco_mix['ingridients']:
        report+= f"{100//len(tobacco_mix['ingridients'])}% табака {ingridient['tobacco_brand']} со вкусом {ingridient['tobacco_flavor']} "
        pot.append(ingridient['tobacco_pot'])
    report+= f"\nПодходящие чаши: {' '.join(i for i in set(pot))}"
    return report

def make_tabacco_mix(tobacco_list, ingridients_number, requested_flavor):
    requested_tobaccos = []
    not_requested_tabaccos = []
    for tobacco in tobacco_list:
        if tobacco['tobacco_flavor'] == requested_flavor:
            requested_tobaccos.append(tobacco)
        else:
            not_requested_tabaccos.append(tobacco)
    return random.sample(requested_tobaccos,1) + random.sample(not_requested_tabaccos, ingridients_number-1)
# запросить у пользователя количество вкусов в миксе
# запросить желаемый вкус в миксе
# обойти исходный список полностью и в новый подсписок взять элементы только с запрошенным ключом вкуса
# получить подсписок из исходного с вычетом предыдущего подсписка
# вернуть элемент из первого подсписка и недостающие из второго
 
if __name__ == "__main__":
    # 1. Read file line by line
    with open("./raw_data/tobacco.txt") as raw_tobacco_data_file:
        raw_tobacco_data = raw_tobacco_data_file.readlines()
    
    # 2. Split line from file by "," separator
    # 3. Write splitted data to dict
    # 4. Save dict into list
    tobacco_list = [
        {
            "tobacco_brand": tobacco_string.split(",")[0],
            "tobacco_flavor": tobacco_string.split(",")[1],
            "tobbacco_strength": tobacco_string.split(",")[2],
            "tobacco_pot": tobacco_string.split(",")[3].replace("\n", "")
        }
        for
        tobacco_string in
        raw_tobacco_data
    ]

    # 5. Get combination of two random list elements
    
    # 6. Save combination into another dict
    # tobacco_mix = {
    #     "ingridients": simple_mix[0],
    #     "rating": simple_mix[1],
    #     "third_tabacco": simple_mix[2]
    # }


    # 7. Add rating to combination
    
    tobacco_mix = {
        'ingridients': make_tabacco_mix(tobacco_list, 3, 'Кола'),
        'rating': random.randint(0, 100)
    }
    
    # 8. Save all of this as json
    with open("./output/mixes_data/new_mix.json", "w") as mix_file:
        json.dump(tobacco_mix, mix_file)
    
    with open("./output/tobacco_data/tobaccos.json", "w") as mix_file:
        json.dump(tobacco_list, mix_file)
    
    print(generate_report(tobacco_mix))
