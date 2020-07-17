# Pygame Utils
A compilation of utility tools (mainly widgets: buttons, checkboxes...) to use with [pygame](https://www.pygame.org/). 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygame Utils.
```bash
pip install utils-pygame 
```

## Usage
So far there are 2 widgets: `button` and `checkbox`
Every widget has a `draw` function, that draws the widget. To use it simply call `
yourWidget.draw(win)`, where `yourWidget` corresponds to your widget name and `win` corresponds to your pygame display.

In almost every widget you don't need to specify every single attribute, default values are used instead.

You can run the `example.py` file to get a general idea of what the widgets look like as well as using it as a reference or template.

#### Some common concepts across widgets

| Concept | Description | Type |
| :---: | --- | :---: |
| `color` | Color of the widget | (int, int, int) |
| `x` | X coordinate (top left corner) | int |
| `y` | Y coordinate (top left corner) | int |
| `width` | Width of the widget | int |
| `height` | Height of the widget | int |

 
### Button
#### Creating a button:
```python
import PygameUtils as pu
but = pu.button(color, x, y, width, height)
```
#### Optional arguments:

| Argument | Description | Type | Default Value |
| :---: | --- | :---: | :---: |
| `text` | Text displayed in the middle | str | "" |
| `size` | Size of the text | int | 60 |
| `font` | Name of the font to use (system font) | str | None
| `outline` | Outline of the button | int | 0

#### Interacting with a button:
Using the `isOver(pos)` function, you can check if a given position (`(x, y)` tuple, most likely the position of the mouse) is over the button, associating all kinds of pygame events to it (`pygame.MOUSEBUTTONDOWN`, `pygame.MOUSEMOTION`).

### Checkbox
#### Creating a checkbox:
```python
import PygameUtils as pu
checkb = pu.checkbox(color, x, y, width, height)
```
#### Optional arguments:

| Argument | Description | Type | Default Value |
| :---: | --- | :---: | :---: |
| `outline` | Outline of the box | int | 1 |
| `check` | Size of the text | bool | False |
| `text` | Text displayed to the right | str | ""
| `size` | Size of the text | int | 60
| `font` | Name of the font to use (system font) | str | None
| `textGap` | Gap between the text and the box | int | 10

#### Interacting with a checkbox:
Like the button, you can use the `isOver(pos)` function to check if a given position is over the box.

The `convert()` function changes the state of the box, from checked to unchecked or vice versa. Most likely you will want to use this function alongside the `isOver(pos)` function and the `pygame.MOUSEBUTTONDOWN` event.

The `isChecked()` function returns the current state of the box (`True` if checked, `False` otherwise)

## License
[MIT](https://choosealicense.com/licenses/mit/)
