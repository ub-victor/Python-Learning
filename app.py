from pathlib import Path

from  ecommerce.shipping import calc_shipping

calc_shipping()
path = Path('ecommerce') # ecommerce folder in the current directory
create = path("email")
print(create.mkdir())



