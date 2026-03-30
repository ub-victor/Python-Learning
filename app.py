from pathlib import Path

from  ecommerce.shipping import calc_shipping

calc_shipping()
path = Path('ecommerce') # 
print(path.exists())



