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
    return f"Чтобы сделать этот крутой микс, возьмите 50% табака {tobacco_mix[0]['tobacco_brand']} со вкусом {tobacco_mix[0]['tobacco_flavor']}, добавьте 50% табака {tobacco_mix[1]['tobacco_brand']} со вкусом {tobacco_mix[1]['tobacco_flavor']}, используйте чашу {tobacco_mix[0]['tobacco_pot']} или {tobacco_mix[1]['tobacco_pot']}"


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
    simple_mix = random.sample(tobacco_list, 2)
    
    # 6. Save combination into another dict
    tobacco_mix = {
        "first_tobacco": simple_mix[0],
        "second_tobacco": simple_mix[1],
    }

    # 7. Add rating to combination
    tobacco_mix["rating"] = random.randint(0, 100)

    # 8. Save all of this as json
    with open("./output/mixes_data/new_mix.json", "w") as mix_file:
        json.dump(tobacco_mix, mix_file)
    
    with open("./output/tobacco_data/tobaccos.json", "w") as mix_file:
        json.dump(tobacco_list, mix_file)
    
    print(generate_report(simple_mix))
