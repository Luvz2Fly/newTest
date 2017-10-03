fred = "Why do deer have big noses"
print(fred)
print(fred)

print("This is a \"test\" of strings")

myScore = 1000
sport = "basketball"
message = 'I scored %s points in %s'
print(message % (myScore, sport))


joke = '%s: a device for finding furniture in the dark'
part1 = 'Knee'
part2 = 'Shin'
print(joke % part2)

print(10 * 'a')

spaces = " " * 25
print('%s 12 Butt Wynd' % spaces)
print('%s West Snoring' % spaces)

# print(1000 * 'snirt\n')

wizard_list = ['spider legs', 'toe of frogs', 'eye of newt', 'bat wing',
               'slug butter', 'snake dandruff']
print(wizard_list)
print(wizard_list[2])
wizard_list[2] = 'snail tounge'
print(wizard_list[2])

print(wizard_list[2:5])
print()

numbers = [1, 2, 3, 4]
strings = ['I', 'Kicked', 'My', 'Toe', 'and', 'It', 'Is', 'Sore']
mylist = [numbers, strings]
print(mylist)
print(mylist[1][2])

wizard_list.append('bear burp')
print(wizard_list)
del wizard_list[5]
print(wizard_list)

wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

print()

list1 = [1, 2, 3, 4]
list2 = ['I', 'Kicked', 'My', 'Toe', 'and', 'It', 'Is', 'Sore']
list3 = list1 + list2
print(list3)

print(list2 * 5)

fibs = (0, 1, 1, 2, 3)
print(fibs)

print()

favorite_sports = {'Ralph William': 'Football',
                   'Michael Tipper': 'Basketball',
                   'Edward Elgar': 'Baseball',
                   'Rebecca Clark': 'Netball',
                   'Ethel Smyth': 'Badmitten',
                   'Frank Bridge': 'Rugby'}
print(favorite_sports['Rebecca Clark'])
print(favorite_sports)
print()
favorite_sports['Ralph William'] = 'Ice Hockey'
print(favorite_sports)
print()

for x in range(0, 5):
    print("hello")

for y in range(0, 10):
    print(y)

print()

print(list(range(10, 20)))

for x in range(0, 5):
    print('hello %s' % x)

print()

for i in wizard_list:
    print(i)
    print(i)
print()
print()
print("=====================")

hhp = ['huge', 'hairy', 'pants']
for i in hhp:
    print(i)
    for j in hhp:
        print(j)

print()
print()
print("=====================")

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))


def lineBreak(count: object) -> object:
    if count > 0:
        print(count * "=")
    else:
        print(15 * "=")


for x in range(1, 10):
    lineBreak(x)


print("GITHUB PUSH TEST")
