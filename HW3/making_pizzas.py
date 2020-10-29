import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green chile', 'extra cheese')

from pizza import make_pizza
make_pizza(10, 'garlic')

from pizza import make_pizza as mp
mp(8, 'sausage')

import pizza as p
p.make_pizza(6, 'shrimp')

from pizza import *
make_pizza(69, 'humongus')