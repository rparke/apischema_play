FROM continuumio/miniconda:4.7.12
RUN cd /home && git clone https://github.com/rparke/apischema_play 
RUN cd /home/APISCHEMA_PLAY && conda env create -f environment.yml
CMD bash