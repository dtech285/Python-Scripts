#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

'''asdf
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelaceasdf
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")
message = "Hello, " +  full_name.title() + "!"
print(message)
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
'''

#print('Albert Einstein once said "A person who never made a mistake never tried anything new"')
#Quote = 'Albert Einstein once said "A person who never made a mistake never tried anything new"'
#print(Quote)

motorcycles = ['Honda', 'Yamaha', 'Susuki']
print(motorcycles)

#motorcycles[0] = 'Ducati'
motorcycles.append('Ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles.append('Yamaha')
print(motorcycles)

motorcycles.remove('Yamaha')
print(motorcycles)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print()

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\n....and the original list again")
print(cars)
