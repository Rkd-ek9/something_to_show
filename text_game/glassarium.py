glassarium = {
    "enemies": [
        {"name": "Волк",
         "hp": "rd(20, 23) + sum([rd(3,5) for _ in range(lvl)])",
         "acts": [{"disc": "Волк готовится напрыгнуть на вас",
                   "type": "Heavy",
                   "dmg": "lvl * 1.5 + rd(1,5)",
                   "cool": 3},

                  {"disc": "Волк готовится бежать на вас",
                   "type": "Light",
                   "dmg": "lvl * 0.5 + 3",
                   "cool": 1},

                  {"disc": "Волк насторожился",
                   "type": "Parry",
                   "dmg": "lvl * 0.5 + 4",
                   "cool": 2}],

         "mods": {
             "Бешенный волк": {
                 "hp": "self.health // 2",
                 "acts": [
                     {"disc": "Волк готовится напрыгнуть на вас",
                      "type": "Heavy",
                      "dmg": "lvl * 1.5 + rd(1,5)",
                      "cool": 3},

                     {"disc": "Волк готовится бежать на вас",
                      "type": "Light",
                      "dmg": "lvl * 0.5 + 3",
                      "cool": 1},

                     {"disc": "Волк насторожился",
                      "type": "Parry",
                      "dmg": "lvl * 0.5 + 4",
                      "cool": 2}]
                 }
             }
         },

        {"name": "Скелет",
         "hp": "rd(10, 12) + sum([rd(2,6) for _ in range(lvl)])",
         "acts": [{"disc": "Скелет взял левую руку в правую",
                   "type": "Heavy",
                   "dmg": "lvl * rd(2,5)",
                   "cool": 2},

                  {"disc": "Скелет поднял камешек и замахнулся",
                   "type": "Light",
                   "dmg": "lvl * rd(1,4)",
                   "cool": 1}]}],

    "non_random_enemies": [
        {
            "name": "Мимик",
            "hp": "rd(20, 40) + rd(2, 6) * lvl",
            "acts": [{"disc": "Мимик оскалился на вас",
                      "type": "Heavy",
                      "dmg": "lvl * 2 + rd(2,5)",
                      "cool": 3},

                     {"disc": "Мимик скачет в вашу сторону",
                      "type": "Light",
                      "dmg": "lvl * 1 + 3.5",
                      "cool": 1}]
        }
    ],

    "hero": {
        "knight": {
            "name": "Рыцарь",

            "feature": {
                "heavy": "+1",
                "light": "+1",
                "parry": "+1",
                "resist": "+3"
            },
            "skills": [{"disc": "Тяжёлая атака",
                        "type": "Heavy",
                        "dmg": "6 + lvl * 2 + heavy",
                        "cool": 5},

                       {"disc": "Быстрая атака",
                        "type": "Light",
                        "dmg": "3 + lvl * 1 + light"},

                       {"disc": "Парирование",
                        "type": "Parry",
                        "dmg": "lvl * 1.5 + 4 + parry"},

                       {"disc": "Защита",
                        "type": "Resist",
                        "dmg": "0"}],

            "intro": """Вы просыпаетесь от глубокого сна, 
вы не помните что было до него и кажется, что это не так уж и важно.
Вы одеты в местами проржавешую броню, при вас ваш потрёпанный меч.
Вы не видете иного пути кроме как идти вперёд.""",

            "base_weapon": {
                "name": "Потрёпанный меч",
                "heavy": "0",
                "light": "0",
                "parry": "0",
                "resist": "0"
            },

            "base_armor": {
                "name": "Ржавая броня",
                "heavy": "0",
                "light": "0",
                "parry": "0",
                "resist": "+1"
            },

            "base_health": 20
        },
    },
    "weapon": {
        "common": [
            {
                "name": "Ржавый меч",
                "heavy": "+3",
                "light": "0",
                "parry": "-2",
                "resist": "3"
            },
            {'name': 'Искривлённый меч', 'heavy': "3", 'light': "1", 'parry': "0", 'resist': "0"},
            {'name': 'Дубинка', 'heavy': "3", 'light': "-2", 'parry': "-2", 'resist': "3"},
            {'name': 'Обломанный меч', 'heavy': "2", 'light': "1", 'parry': "0", 'resist': "1"},
            {"name": "Гиганский меч", 'heavy': '9', 'light': '-2', 'parry': "-2", 'resist': "-2"}
        ],
        "uncommon": [
            {
                "name": "Рыцарский",
                "heavy": "+2",
                "light": "+1",
                "parry": "+1",
                "resist": "1"
            },
            {"name": "Бревно", 'heavy': "6", 'light': "0", 'parry': "0", 'resist': "2"},
            {'name': 'Защитные перчатки', 'heavy': "4", 'light': "-2", 'parry': "-2", 'resist': "5"}
        ],
        "legendary": [
            {
                "name": "Звёздный",
                "heavy": "-1",
                "light": "+8",
                "parry": "0",
                "resist": "5"
            },
            {'name': 'Меч баланса', 'heavy': '5', 'light': '5', 'parry': '3', 'resist': '0'},
            {'name': 'Меч-гора', 'heavy': '12', 'light': '-5', 'parry': '-3', 'resist': '2'},
            {'name': 'Меч молнии', 'heavy': '-5', 'light': '8', 'parry': '6', 'resist': '4'}
        ]
    },
    "armor": {
        "common": [
            {
                "name": "Ржавая",
                "heavy": "+2",
                "light": "0",
                "parry": "0",
                "resist": "-2"
            },
            {'name': '-3', 'heavy': '-2', 'light': '0', 'parry': '1', 'resist': '4'}
        ],
        "uncommon": [
            {
                "name": "Рыцарская броня",
                "heavy": "+2",
                "light": "+1",
                "parry": "+1",
                "resist": "1"
            },
            {'name': 'Лёгкая броня', 'heavy': '1', 'light': '3', 'parry': '2', 'resist': '0'},
            {'name': 'Чешуйчатая броня', 'heavy': '4', 'light': '1', 'parry': '-3', 'resist': '2'}
        ],
        "legendary": [
            {
                "name": "Звёздная",
                "heavy": "+4",
                "light": "+8",
                "parry": "+4",
                "resist": "5"
            },
            {'name': 'Сбалансированная броня', 'heavy': '3', 'light': '3', 'parry': '2', 'resist': '4'},
        ]
    },
    "turn": {
        0: """Сумерки, жизнь потихоньку идёт на покой.""",
        5: """За вами очень темно, но можно разглядеть колыщащиеся деревья.""",
        10: "Ваши следы, расплываются во тьме за вами",
        15: "Мира за вами не существует."
    }
}
