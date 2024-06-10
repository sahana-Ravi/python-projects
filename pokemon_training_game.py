"""Problem :
You are a Pokémon trainer. Each Pokémon has its own power, described by a positive integer value. As you travel, you watch Pokémon and you catch each of them. After each catch, you have to display maximum and minimum powers of Pokémon caught so far. You must have linear time complexity. So sorting won’t help here. Try having minimum extra space complexity.

Examples:
Suppose you catch Pokémon of powers 3 8 9 7. Then the output should be
3 3
3 8
3 9
3 9"""
powers = list(input('ENTER POWERS: ').split(' '))
mini, maxi = 1, 1
i = 0
for i in range(len(powers)):
    demo = powers[0:i+1]
    print(min(demo), max(demo))
