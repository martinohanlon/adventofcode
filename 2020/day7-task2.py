# with open("2020/day7testdata2.txt") as f:
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
    
def how_many_bags(bag_rules, bag_contents):
    bag_count = 0
    for bag_color in bag_contents.keys():
        # print(bag_contents[bag_color], bag_color)        
        bag_count += bag_contents[bag_color]
        for i in range(bag_contents[bag_color]):
            bag_count += how_many_bags(bag_rules, bag_rules[bag_color])

    return bag_count

bag_count = how_many_bags(bag_rules, bag_rules["shiny gold"])

print(bag_count)