# with open("2020/day7testdata.txt") as f:
with open("2020/day7bagrules.txt") as f:
    data = f.read().splitlines() 

bag_rules = {}
for line in data:
    bag_name, raw_contains = line.split(" bags contain ")
    # print(bag_name,raw_contains)
    raw_contains = raw_contains.split(",")

    bag_contains = {}
    for item in raw_contains:
        item = item.strip()
        if "no other bags" in item:
            number_of_bags = 0
        else:
            number_of_bags = int(item[0])
            end_pos_of_bag_type = item.find(" ", 2) + 1
            end_pos_of_bag_color = item.find(" ", end_pos_of_bag_type)
            bag_color = item[2:end_pos_of_bag_color]
            bag_contains[bag_color] = number_of_bags
        
    bag_rules[bag_name] = bag_contains
    
# print(bag_rules)

def contains_bag(bag_rules, bag_contents, bag_to_find):
    found_bag = False
    if bag_to_find in bag_contents.keys():
        found_bag = True
    for bag_color in bag_contents.keys():
        if contains_bag(bag_rules, bag_rules[bag_color], bag_to_find):
            found_bag = True
    return found_bag
    
# look for shiny gold bags
shiny_gold_count = 0
for bag_color in bag_rules.keys():
    shiny_gold_found = False
    if contains_bag(bag_rules, bag_rules[bag_color], "shiny gold"):
        shiny_gold_found = True

    if shiny_gold_found:
        shiny_gold_count += 1

print(shiny_gold_count)