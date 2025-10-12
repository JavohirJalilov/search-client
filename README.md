# Face Search Client

## create and activate envorment

```bash
python3 -m venv venv
source venv/bin/activate
```
## install requirements

```bash
pip install -r requirements.txt
```

## search 

```bash
python search.py <image path>
```

## example

```bash
python search.py images/image.jpg
```

```json
{
  "results": [
    [
      {
        "first_name": "Salimjonov",
        "last_name": "Murodjon Alimjon o'g'li",
        "score": 0.5786024928092957,
        "ids": "1896",
        "profile_picture": "https://cdn.absvision.ai/reportemployee/1/a69129b6f2ff429dbda1a79aaf0e3dd5.jpg"
      }
    ],
    [
      {
        "first_name": "Gafirov",
        "last_name": "Avazbek Zaytbay o'g'li",
        "score": 0.8144222497940063,
        "ids": "1715",
        "profile_picture": "https://cdn.absvision.ai/reportemployee/1/17604e56a426496c8f8b3dee245904c9.jpg"
      }
    ],
    [
      {
        "first_name": "Abduxakimov",
        "last_name": "Javlonbek Abdulatifovich",
        "score": 0.7734742760658264,
        "ids": "2047",
        "profile_picture": "https://cdn.absvision.ai/reportemployee/1/2d97d2ac6e5e4571860a5df282a1a8ab.jpg"
      }
    ]
  ]
}
```