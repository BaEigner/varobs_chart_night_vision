# varobs_chart_night_vision
Turns regulat b&amp;w AAVSO variable ovservation charts to red&amp;black for night view.

Python 3 and Pillow package needed: 
```
pip install pillow
```

Parameters:
* 1st: file path/name, e.g. X38343IA.png (mandatory)
* 2nd: preview flag: "show" if you want to automatically open the generated image

If ran successfully, generates file with "_NV" postfix ("night vision"), e.g. X38343IA.png >>> X38343IA_NV.png
  
Usage:

```
python chart_red.py X38343IA.png
```
or
```
python chart_red.py X38343IA.png show
```
