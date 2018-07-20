FROM python:2

ARG APP_PATH=/hardware-checkout

WORKDIR $APP_PATH

ADD requirements.txt $APP_PATH
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . $APP_PATH

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "-k", "eventlet", "hardwarecheckout:app"]
