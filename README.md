<img align="right" width="200" src="https://treecoin.online/wp-content/uploads/2021/07/spring_250.png">

# Tree Coin logo drawer
This script uses [Python Turtle](https://docs.python.org/3/library/turtle.html) to draw the Tree Coin logo.<br />
Colours are based on the current season and are divided as follow:

### Branch colours
| Winter    | Spring    | Summer    | Autumn    |
|:---------:|:---------:|:---------:|:---------:|
| ![#45613d](https://via.placeholder.com/15/45613d/000000?text=+) `#45613d` | ![#788e2f](https://via.placeholder.com/15/788e2f/000000?text=+) `#788e2f` | ![#566d2e](https://via.placeholder.com/15/566d2e/000000?text=+) `#566d2e` | ![#45613d](https://via.placeholder.com/15/45613d/000000?text=+) `#45613d` |
| ![#334729](https://via.placeholder.com/15/334729/000000?text=+) `#334729` | ![#566d2e](https://via.placeholder.com/15/566d2e/000000?text=+) `#566d2e` | ![#45613d](https://via.placeholder.com/15/45613d/000000?text=+) `#45613d` | ![#334729](https://via.placeholder.com/15/334729/000000?text=+) `#334729` |
| ![#454524](https://via.placeholder.com/15/454524/000000?text=+) `#454524` | ![#45613d](https://via.placeholder.com/15/45613d/000000?text=+) `#45613d` | ![#334729](https://via.placeholder.com/15/334729/000000?text=+) `#334729` | ![#454524](https://via.placeholder.com/15/454524/000000?text=+) `#454524` |
| ![#4b3830](https://via.placeholder.com/15/4b3830/000000?text=+) `#4b3830` | ![#334729](https://via.placeholder.com/15/334729/000000?text=+) `#334729` | ![#454524](https://via.placeholder.com/15/454524/000000?text=+) `#454524` | ![#4b3830](https://via.placeholder.com/15/4b3830/000000?text=+) `#4b3830` |
|           | ![#454524](https://via.placeholder.com/15/454524/000000?text=+) `#454524` | ![#4b3830](https://via.placeholder.com/15/4b3830/000000?text=+) `#4b3830` |           |
|           | ![#4b3830](https://via.placeholder.com/15/4b3830/000000?text=+) `#4b3830` |           |           |

### Leaf colours
| Winter    | Spring    | Summer    | Autumn    |
|:---------:|:---------:|:---------:|:---------:|
| `#dfe7fd` | `#007f5f` | `#ff4800` | `#b1150c` |
| `#eae4e9` | `#2b9348` | `#ff5400` | `#970f08` |
| `#fcf7f8` | `#55a630` | `#ff6000` | `#7c0903` |
| `#f0efeb` | `#80b918` | `#ff6d00` | `#6a1609` |
| `#e2ece9` | `#aacc00` | `#ff7900` | `#4b1101` |
| `#d0e7e8` | `#bfd200` | `#ff8500` | `#652c18` |
| `#bee1e6` | `#d4d700` | `#ff9100` | `#773c07` |
| `#cfdbcc` | `#dddf00` | `#ff9e00` | `#a46728` |
| `#eff2ef` | `#eeef20` | `#ffaa00` | `#d69c52` |
| `#e7ede6` | `#ffff3f` | `#ffb600` | `#daa562` |
|           |           | `#dddf00` |           |
|           |           | `#eeef20` |           |
|           |           | `#ffff3f` |           |

The file [`logo_generator.py`](https://github.com/Tree-Coin/Logo/blob/master/logo_generator.py) contains the [`main()`](https://github.com/Tree-Coin/Logo/blob/b7bed7a6cfe6d04c17b377b3c0d891d67bcaaf46/logo_generator.py#L162-L216) function that [`draw roots`](https://github.com/Tree-Coin/Logo/blob/b7bed7a6cfe6d04c17b377b3c0d891d67bcaaf46/logo_generator.py#L202) and then [`the tree`](https://github.com/Tree-Coin/Logo/blob/b7bed7a6cfe6d04c17b377b3c0d891d67bcaaf46/logo_generator.py#L209).

The [`roots` function](https://github.com/Tree-Coin/Logo/blob/b7bed7a6cfe6d04c17b377b3c0d891d67bcaaf46/roots.py#L21) and the [`tree` function](https://github.com/Tree-Coin/Logo/blob/b7bed7a6cfe6d04c17b377b3c0d891d67bcaaf46/tree.py#L22) are recursive functions, and placed in their respective files.
<br>
<br>
<br>

## How to launch this program:

Just type:
```
$> python3 logo_generator.py
```


