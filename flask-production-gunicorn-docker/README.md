- Add a new virtual environment using a tool of your choosing:
```
> python -m venv .venv
> (activate it according to your os, win: .venv\Scripts\activate)
```

- To run locally:
```
> cd src
> flask -A local run
```

- Run in docker:
```
> docker build -t <ImageName>:latest .
> docker run -p 5001:8000 <ImageName>:latest
(internal port must be mapped to external port to be accessible)
```

- Install gunicorn
```
> pip install gunicorn
```

- We can add a small shell script to instruct gunicorn to read the config file an run the app:
- refer to src/gunicorn.sh