FROM TeamTandav x/TANDAV X-USERBOT:latest

#clonning repo 
RUN git clone https://github.com/SHIVGULSHAN/TANDAV-X-USERBOT.git /root/DYNAMIC
#working directory 
WORKDIR /root/DYNAMIC

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/DYNAMIC/bin:$PATH"

CMD ["python3","-m","DYNAMIC"]
