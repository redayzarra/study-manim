# Manim Usage Guide

This guide will help you get started with creating animations using Manim. Below are the essential commands you need to know.

## Creating a Manim Scene

My custom user snippet for starting a new `scene.py` is:

```python
goman
```

Which effectively types:
```python
from manim import *

class ClassName(Scene):
    def construct(self):

```

## Running Manim
In the terminal, I need to go to the directory of `scene.py` and type:

```bash
manim scene.py [Class name]
```
or alternatively

```bash
python -m manim scene.py [Class name]
```

## Video Settings
For **Low Quality** preview videos:
```bash
manim -pql scene.py [Class name]
```

For **High Quality** final videos:
```bash
manim -pqk scene.py [Class name]
```

To change the aspect ratio and resolution of videos add this:

```python
from manim import *

# For vertical content
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class ClassName(Scene):
    def construct(self):

```

## Creating a GIF's
I can also create GIF's of different qualities with the flag:
```bash
manim --format=gif scene.py [Class name]
```
## Getting last frame
You can get the last frame of scene with:
```bash
manim -sqk scene.py [Class name]
```
