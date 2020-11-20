FROM lsuazo/pythondjango

COPY . /usr/src/AsYouWish
WORKDIR /usr/src/AsYouWish
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
