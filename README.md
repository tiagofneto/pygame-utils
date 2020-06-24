# Pygame Utils
A compilation of utility tools (mainly widgets: buttons, checkboxes...) to use with [pygame](https://www.pygame.org/). 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygame Utils.
```bash
pip install utils-pygame 
```

## Usage
So far there are 2 widgets: ```button``` and ```checkbox```
Every widget has a ```draw``` function, that draws the widget. To use it simply call ```
yourWidget.draw(win)```, where ```yourWidget``` corresponds to your widget name and ```win``` corresponds to your pygame display.

In almost every widget you don't need to specify every single attribute, default values are used instead.

You can run the ```example.py``` file to get a general idea of what the widgets look like as well as using it as a reference or template.

#### Some common concepts across widgets:
* ```color```: RGB tuple (ex: ```(125, 100, 200)```)
* ```x```: x coordinate
* ```y```: y coordinate
* ```width```: width of the widget
* ```height```: height of the widget
* ```text```: text associated with the widget
* ```size```: size of the text
* ```font```: name of the font to use (make sure it is installed in your system)
* ```outline```: the outline of the widget
 
### Button
#### Creating a button:
```python
import PygameUtils as pu
but = pu.button(color, x, y, width, height)
```
#### Optional arguments:
* ```text```
* ```size```
* ```font``` 
* ```outline```

#### Interacting with a button:
Using the ```isOver(pos)``` function, you can check if a given position (```(x, y)``` tuple, most likely the position of the mouse) is over the button, associating all kinds of pygame events to it (```pygame.MOUSEBUTTONDOWN```, ```pygame.MOUSEMOTION```).

### Checkbox
#### Creating a checkbox:
```python
import PygameUtils as pu
checkb = pu.checkbox(color, x, y, width, height)
```
#### Optional arguments:
* ```outline```
* ```check```: if the box starts checked or not (```boolean```)
* ```text```
* ```size```
* ```font``` 
* ```textGap```: the amount of space between the text and the box

#### Interacting with a checkbox:
Like the button, you can use the ```isOver(pos)``` function to check if a given position is over the box.

The ```convert()``` function changes the state of the box, from checked to unchecked or vice versa. Most likely you will want to use this function alongside the ```isOver(pos)``` function and the ```pygame.MOUSEBUTTONDOWN``` event.

The ```isChecked()``` function returns the current state of the box (```True``` if checked, ```False``` otherwise)

## License
[MIT](https://choosealicense.com/licenses/mit/)
