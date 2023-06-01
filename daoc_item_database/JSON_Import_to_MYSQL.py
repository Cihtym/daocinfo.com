import json
import mysql.connector

# Specify the MySQL server connection details
config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'DAoC'
}

# Establish a connection to the MySQL server
conn = mysql.connector.connect(**config)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Drop dependent tables first
cur.execute("DROP TABLE IF EXISTS json_05232023.requirements;")
cur.execute("DROP TABLE IF EXISTS json_05232023.abilities;")
cur.execute("DROP TABLE IF EXISTS json_05232023.item_source;")
cur.execute("DROP TABLE IF EXISTS json_05232023.type_data;")
cur.execute("DROP TABLE IF EXISTS json_05232023.items;")
cur.execute("DROP TABLE IF EXISTS json_05232023.bonuses;")
cur.execute("DROP TABLE IF EXISTS json_05232023.slot;")
cur.execute("DROP TABLE IF EXISTS json_05232023.categories;")
cur.execute("DROP TABLE IF EXISTS json_05232023.realm;")
cur.execute("DROP TABLE IF EXISTS json_05232023.bonus_types;")
cur.execute("DROP TABLE IF EXISTS json_05232023.spell_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.position_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.magic_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.class_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.skill_used_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.left_hand_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.two_hand_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.damage_type;")
cur.execute("DROP TABLE IF EXISTS json_05232023.utility_values;")
cur.execute("DROP TABLE IF EXISTS json_05232023.armor_type;")

# Create realm table - this table provides which realm an item is in
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.realm ( \
    realm_id INT NOT NULL, \
    realm_name VARCHAR(255) NOT NULL DEFAULT '', \
    PRIMARY KEY(realm_id) \
);")

# Create categories table - this table gives which category an item is, such as armor, weapon, jewelry, etc.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.categories ( \
    category_id INT NOT NULL, \
    category_name VARCHAR(255) NOT NULL DEFAULT '', \
    PRIMARY KEY(category_id) \
);")

# Create slot table - this table gives which slot an item goes into, left bracer, right bracer, etc.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.slot ( \
    slot_id INT NOT NULL, \
    slot_name VARCHAR(255) NOT NULL DEFAULT 'unknown', \
    PRIMARY KEY(slot_id) \
);")

# Create utility_values table - this table provides the utility values for each statistic/ToA stat; used to calculate total item utility
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.utility_values ( \
            bonus_id INT PRIMARY KEY AUTO_INCREMENT, \
            utility_value FLOAT \
);")
        
# Create bonus_types  - Table that gives exactly what bonus an item has. This is strength, dex, slash resist, magic damage, etc. The SC and ToA stats an item can have. This table is also used in the calculation of the utility value.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.bonus_types ( \
    bonus_type_id INT PRIMARY KEY AUTO_INCREMENT, \
    bonus_id INT NOT NULL REFERENCES json_05232023.utility_values(bonus_id), \
    bonus_type VARCHAR(255) NOT NULL, \
    sub_name VARCHAR(255) \
);")

# Create items table - Table that gives the item name, category, realm, slot, icon to search for skins, bonus level, and utility value.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.items ( \
    item_id INT PRIMARY KEY AUTO_INCREMENT, \
    item_name VARCHAR(255) NOT NULL DEFAULT '', \
    category_id INT NOT NULL REFERENCES json_05232023.categories(category_id), \
    realm_id INT NOT NULL REFERENCES json_05232023.realm(realm_id), \
    slot_id INT REFERENCES json_05232023.slot(slot_id), \
    icon INT NOT NULL, \
    bonus_level INT, \
    utility FLOAT \
);")

# Create class_type table - Table that returns the class requirement id values. Guardian and Naturalist classes were added manually
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.class_type ( \
            class_requirement_id INT PRIMARY KEY AUTO_INCREMENT, \
            class_requirement_desc VARCHAR(255));")

# Create requirements table - Table giving class and level requirements for an item
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.requirements ( \
    requirement_id INT PRIMARY KEY AUTO_INCREMENT, \
    item_id INT REFERENCES json_05232023.items(item_id), \
    class_requirement_id INT REFERENCES json_05232023.class_type(class_requirement_id), \
    level_requirement INT);")

# Create spell_type table - The exact text for what the proc description is.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.spell_type ( \
            spell_id INT PRIMARY KEY AUTO_INCREMENT, \
            spell_desc VARCHAR(255) NOT NULL \
            );")
    
# Create position_type table - Table that provides /use1 or /use2 reference
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.position_type ( \
                position_id INT PRIMARY KEY AUTO_INCREMENT,\
                position_name VARCHAR(255) NOT NULL\
            );")

# Create magic_type table - Table that provides what type of proc an item is, offensive, defensive, whether it needs to be worn, and whether it's a charge.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.magic_type ( \
                magic_type_id INT PRIMARY KEY AUTO_INCREMENT, \
                magic_type_name VARCHAR(255) NOT NULL \
            );")

# Create damage_type table - Available damage types, slash crush thrust etc. Doesn't include all damage types as BS didn't include the full list in the metadata file
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.damage_type ( \
                damage_type_id INT PRIMARY KEY AUTO_INCREMENT, \
                damage_type_desc VARCHAR(255) NOT NULL \
            );")
    
# Create abilities table - Contains information about the procs an item has, what spell they are, what level requirement to use it (power_level) and whether it's offensive or defensive.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.abilities ( \
    ability_id INT PRIMARY KEY AUTO_INCREMENT, \
    item_id INT REFERENCES json_05232023.items(item_id), \
    spell_id INT NOT NULL REFERENCES json_05232023.spell_type(spell_id), \
    position_id INT NOT NULL REFERENCES json_05232023.position_type(position_id), \
    power_level INT, \
    magic_type_id INT NOT NULL REFERENCES json_05232023.magic_type(magic_type_id) \
);")
            
# Create item_source table - Table that gives the mob that drops an item. source_type gives whether it's a drop or quest item and source_name is the NPC name
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.item_source ( \
    source_id INT PRIMARY KEY AUTO_INCREMENT, \
    item_id INT REFERENCES json_05232023.items(item_id), \
    source_type VARCHAR(255) NOT NULL, \
    source_name VARCHAR(255) NOT NULL \
);")

# Create skill_used_type table - Indicates what skill is required to use the item. This is useful to find swords, axes, thrust weapons, etc. Realm specific as it is name specific, i.e. not swords on Hib, blades.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.skill_used_type ( \
            skill_used_id INT PRIMARY KEY AUTO_INCREMENT, \
            skill_used_name VARCHAR(255) NOT NULL \
            );")

# Create left_hand_type table - Reference table for whether an item is left hand usable
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.left_hand_type ( \
            left_hand_id INT PRIMARY KEY AUTO_INCREMENT, \
            left_hand_desc BOOLEAN NOT NULL \
            );")

# Create two_hand_type table - Reference table for whether an item is a two-handed weapon
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.two_hand_type ( \
            two_hand_id INT PRIMARY KEY AUTO_INCREMENT, \
            two_hand_desc BOOLEAN NOT NULL \
            );")

# Create armour_type table - Reference Table for the armor types. Not split between hib and the other realms.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.armour_type ( \
            armour_type_id INT PRIMARY KEY AUTO_INCREMENT, \
            armour_type_desc VARCHAR(255) NOT NULL \
            );")

# Insert values into armour_type table - Note the Chain/Scale.
cur.execute("INSERT INTO json_05232023.armour_type (armour_type_id, armour_type_desc) \
    VALUES \
        (0, 'Cloth'), \
        (10, 'Leather'), \
        (19, 'Studded/Reinforced'), \
        (27, 'Chain/Scale'), \
        (34, 'Plate');")
        
# Create type_data table - This is the main table for armor and weapons, what kind of armor, what kind of weapons, weapon speed, etc.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.type_data ( \
    type_data_id INT PRIMARY KEY AUTO_INCREMENT, \
    item_id INT REFERENCES json_05232023.items(item_id), \
    armor_factor INT, \
    clamped_armor_factor INT, \
    absorption INT REFERENCES json_05232023.armour_type(armour_type_id), \
    base_quality INT, \
    dps FLOAT, \
    clamped_dps FLOAT, \
    speed INT, \
    damage_type INT REFERENCES json_05232023.damage_type(damage_type_id), \
    two_handed INT REFERENCES json_05232023.two_hand_type(two_hand_id), \
    left_handed INT REFERENCES json_05232023.left_hand_type(left_hand_id), \
    skill_used INT REFERENCES json_05232023.skill_used_type(skill_used_id), \
    level INT \
);")
        
# Create bonuses table - This table lists the statistics on an item and requires the bonus_type table to interpret.
cur.execute("CREATE TABLE IF NOT EXISTS json_05232023.bonuses ( \
    bonus_id INT PRIMARY KEY AUTO_INCREMENT, \
    item_id INT NOT NULL REFERENCES json_05232023.items(item_id), \
    bonus_type_id INT NOT NULL REFERENCES json_05232023.bonus_types(bonus_type_id), \
    bonus_value INT NOT NULL \
);")
        
# Load the JSON file for the Meta Data
with open("Z:/daoc_item_database_combined/daoc_item_metadata.json", "r") as json_file:
    data = json.load(json_file)
    realm_data = data.get("realm", {})
    bonus_types_data = data.get("bonus_types", {})
    categories_data = data.get("categories", {})
    slot_data = data.get("slot", {})
    spell_data = data["abilities"]["spell"]
    position_data = data["abilities"]["position"]
    magic_type_data = data["abilities"]["magic_type"]
    requirements_type_data = data["requirements"]["usable_by"]
    skill_used_type_data = data['bonus_types']['2']['sub_types']
    
# Insert values into realm table
for realm_id, realm_name in realm_data.items():
    cur.execute("INSERT INTO json_05232023.realm (realm_id, realm_name) VALUES (%s, %s);", (int(realm_id), realm_name))

# Insert values into categories table
for categories_id, categories_name in categories_data.items():
    cur.execute("INSERT INTO json_05232023.categories (category_id, category_name) VALUES (%s, %s);", (int(categories_id), categories_name))

# Insert values into slot table
for slot_id, slot_name in slot_data.items():
    cur.execute("INSERT INTO json_05232023.slot (slot_id, slot_name) VALUES (%s, %s);", (int(slot_id), slot_name))

# Insert values into utility_values table
for bonus_id, bonus_data in bonus_types_data.items():
    bonus_name = bonus_data['name']
    if 'utility' in bonus_data:
        utility_value = bonus_data['utility']
        cur.execute("INSERT INTO json_05232023.utility_values (bonus_id, utility_value) VALUES (%s, %s);",
                    (int(bonus_id), utility_value))
    else:
        cur.execute("INSERT INTO json_05232023.utility_values (bonus_id, utility_value) VALUES (%s, '');", (int(bonus_id),))
        
# Insert values into bonus_types table
for bonus_id, bonus_data in bonus_types_data.items():
    bonus_name = bonus_data['name']
    if 'sub_types' in bonus_data:
        for bonus_type, sub_name in bonus_data['sub_types'].items():
            cur.execute("INSERT INTO json_05232023.bonus_types (bonus_id, bonus_type, sub_name) VALUES (%s, %s, %s);",
                        (int(bonus_id), bonus_type, sub_name))
    else:
        cur.execute("INSERT INTO json_05232023.bonus_types (bonus_id, bonus_type) VALUES (%s, '');", (int(bonus_id),))

# Insert values into class_type table
for class_requirement_id, class_requirement_desc in requirements_type_data.items():
    cur.execute("INSERT INTO json_05232023.class_type (class_requirement_id, class_requirement_desc) VALUES (%s, %s);",
                (int(class_requirement_id), class_requirement_desc))

# Insert two additional values into class_type table
cur.execute("INSERT INTO json_05232023.class_type (class_requirement_id, class_requirement_desc) \
            VALUES (%s, %s), (%s, %s);",
            (52, "Guardian", 53, "Naturalist"))
    
# Insert values into spell_type table
for spell_id, spell_desc in spell_data.items():
    cur.execute("INSERT INTO json_05232023.spell_type (spell_id, spell_desc) VALUES (%s, %s);",
                (int(spell_id), spell_desc))
    
# Insert values into position_type table
for position_id, position_name in position_data.items():
    cur.execute("INSERT INTO json_05232023.position_type (position_id, position_name) VALUES (%s, %s);",
                (int(position_id), position_name))

# Insert values into magic_type table
for magic_type_id, magic_type_name in magic_type_data.items():
    cur.execute("INSERT INTO json_05232023.magic_type (magic_type_id, magic_type_name) VALUES (%s, %s);",
                (int(magic_type_id), magic_type_name))

# Insert values into skill_used_type table
for skill_type_id, skill_type_name in skill_used_type_data.items():
    cur.execute("INSERT INTO json_05232023.skill_used_type (skill_used_id, skill_used_name) VALUES (%s, %s);",
                (int(skill_type_id), skill_type_name))

# Insert values into left_hand_type table
cur.execute('''
    INSERT INTO json_05232023.left_hand_type (left_hand_id, left_hand_desc)
    VALUES
        (0, false),
        (1, true);
''')

# Insert values into two_hand_type table
cur.execute('''
    INSERT INTO json_05232023.two_hand_type (two_hand_id, two_hand_desc)
    VALUES
        (0, false),
        (1, true);
''')

# Insert values into damage_type table
cur.execute('''
    INSERT INTO json_05232023.damage_type (damage_type_id, damage_type_desc)
    VALUES
        (1, 'Crush'),
        (2, 'Slash'),
        (3, 'Thrust'),
        (5, 'Siege'),
        (10,'Heat'),
        (12, 'Cold'),
        (17, 'Spirit');
''')

# Load the JSON file for the item database
with open("Z:/daoc_item_database_combined/static_objects.json", "r") as json_file:
    items_data = json.load(json_file)

# Extract the list of items from the dictionary
items_list = items_data['items']

# Insert data into the tables
for item in items_list:
    item_name = item['name']
    category_id = item['category']
    realm_id = item['realm']
    slot_id = item.get('slot')
    icon = item['icon']
    bonus_level = item.get('bonus_level', None)

    cur.execute("INSERT INTO json_05232023.items (item_name, category_id, realm_id, slot_id, icon, bonus_level) \
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING item_id;",
                (item_name, int(category_id), int(realm_id), slot_id, int(icon), bonus_level))

    item_id = cur.fetchone()[0]

    requirements = item.get('requirements', {})
    usable_by = requirements.get('usable_by')
    level_required = requirements.get('level_required')
    
    if level_required:
        cur.execute("INSERT INTO json_05232023.requirements (item_id, level_requirement) \
                    VALUES (%s, %s);",
                   (item_id, int(level_required)))
            
    if usable_by:
        for class_requirement_id in usable_by:
                cur.execute("INSERT INTO json_05232023.requirements (item_id, class_requirement_id) \
                            VALUES (%s, %s);",
                           (item_id, int(class_requirement_id)))

    bonuses = item.get('bonuses', [])
    for bonus in bonuses:
        bonus_type_id = bonus.get('type')
        bonus_value = bonus.get('value')
        cur.execute("INSERT INTO json_05232023.bonuses (item_id, bonus_type_id, bonus_value) VALUES (%s, %s, %s);",
                    (item_id, bonus_type_id, bonus_value))

    abilities = item.get('abilities', [])
    for ability in abilities:
        spell = ability.get('spell')
        position = ability.get('position')
        power_level = ability.get('power_level', None)
        magic_type = ability.get('magic_type')
        cur.execute("INSERT INTO json_05232023.abilities (item_id, spell_id, position_id, power_level, magic_type_id) \
                    VALUES (%s, %s, %s, %s, %s);",
                    (item_id, spell_id, position_id, power_level, magic_type_id))

    sources = item.get('sources', {}).get('monsters', {})
    if 'normal_drop' in sources:
        normal_drop_sources = sources['normal_drop']
        for source_name in normal_drop_sources:
            cur.execute("INSERT INTO json_05232023.item_source (item_id, source_type, source_name) VALUES (%s, %s, %s);",
                        (item_id, 'normal_drop', source_name))

    if 'one_time_drop' in sources:
        one_time_drop_sources = sources['one_time_drop']
        for source_name in one_time_drop_sources:
            cur.execute("INSERT INTO json_05232023.item_source (item_id, source_type, source_name) VALUES (%s, %s, %s);",
                        (item_id, 'one_time_drop', source_name))

    type_data = item.get('type_data', {})
    armor_factor = type_data.get('armor_factor')
    clamped_armor_factor = type_data.get('clamped_armor_factor')
    absorption = type_data.get('absorption')
    base_quality = type_data.get('base_quality')
    dps = type_data.get('dps')
    clamped_dps = type_data.get('clamped_dps')
    speed = type_data.get('speed')
    damage_type = type_data.get('damage_type')
    two_handed = type_data.get('two_handed')
    left_handed = type_data.get('left_handed')
    skill_used = type_data.get('skill_used')
    level = type_data.get('level')

    cur.execute("INSERT INTO json_05232023.type_data (item_id, armor_factor, clamped_armor_factor, absorption, base_quality, \
                dps, clamped_dps, speed, damage_type, two_handed, left_handed, skill_used, level) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (item_id, armor_factor, clamped_armor_factor, absorption, base_quality, dps, clamped_dps, speed, damage_type,
                 two_handed, left_handed, skill_used, level))

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()