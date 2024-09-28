FROM python:3.12

LABEL version="0"
MAINTAINER "Prolog"

EXPOSE 8000/tcp
WORKDIR /
ADD . app


RUN <<EOF
python3 -m venv safe-bike
chmod +x ./safe-bike/bin/activate
./safe-bike/bin/activate
pip3 install -r /app/requirements.txt
EOF

CMD fastapi run
