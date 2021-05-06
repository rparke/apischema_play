FROM continuumio/miniconda:4.7.12
RUN conda create -f environment.yml
RUN CD /home && mkdir APISCHEMA_PLAY
COPY * /home/APISCHEMA_PLAY
CMD conda activate base