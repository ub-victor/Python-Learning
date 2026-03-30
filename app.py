from pathlib import Path

from  ecommerce.shipping import calc_shipping

calc_shipping()
path = Path('ecommerce') # ecommerce folder in the current directory
print(path.exists())



