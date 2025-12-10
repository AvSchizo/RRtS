class skibidiClass:
	value = 1




skibidi = skibidiClass()

toilet = skibidiClass()

toilet.target = skibidi
toilet.target.value += 1


print(toilet.target.value)