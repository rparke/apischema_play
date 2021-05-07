FROM continuumio/miniconda:4.7.12
RUN cd /home && git clone https://github.com/rparke/apischema_play 
RUN conda env create -f /home/apischema_play/environment.yml
CMD bash
