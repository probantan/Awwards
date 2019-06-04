Awwards
===================
## Description
This is Awwwards clone website, where users can post their projects and be rated by other people and those for other people as well


 

------------------------------------------------------------------------

## User Requirements

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page



## Setup

### Requirements
This project should be able to work on different kind of platforms
* Tested on Debian Linux
* Python3.6

### Cloning the repository
```bash
git clone git@github.com:probantan/Awwards.git&& cd personal-gallery
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```
pip3 install -r requirements
```




### Database migrations

``
python manage.py migrate
```


```

### Running the server 
```
python manage.py runserver
```



## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11]
* [Heroku](https://heroku.com)




### License
Copyright (c) {year} **{Morings School}**



## License
MIT License
```
Copyright (c) 2018 Protus Bantan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Copyright (c) 2018 **Protus**
```
