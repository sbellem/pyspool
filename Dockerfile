FROM python:2.7-onbuild

RUN echo America/New_York > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN pip install --upgrade pip
RUN python setup.py install

RUN pip install pytest ipython ipdb

CMD ["py.test", "-v", "tests/"]
