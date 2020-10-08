# pull official base image
FROM python

COPY requirements.txt /requirements.txt

# set working directory
WORKDIR /StudentTicket

# add `/app/venv/.bin` to $PATH
ENV PATH /StudentTicket/venv/bin/activate:$PATH

# install app dependencies
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 8000

# add app
COPY . ./StudentTicket
