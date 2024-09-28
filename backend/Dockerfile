FROM python:3.9

LABEL version="0"
MAINTAINER "Prolog"

EXPOSE 8000/tcp
WORKDIR /
ADD . app


RUN <<EOF
python3 -m venv safe-bike
chmod +x ./safe-bike/bin/activate
./safe-bike/bin/activate
pip3 install osmnx fastapi sqlalchemy
pip3 install "fastapi[standard]"

EOF

CMD fastapi run
