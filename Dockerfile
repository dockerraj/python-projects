FROM python:2.7
RUN apt-get update -y && pip install IPython
ADD tic-tac-toe/tic-tac-toe.py /tmp
CMD python /tmp/tic-tac-toe.py
