FROM python:2.7-onbuild

RUN pip install --upgrade pip
RUN python setup.py install

RUN pip install pytest

CMD ["py.test", "-v", "tests/"]
