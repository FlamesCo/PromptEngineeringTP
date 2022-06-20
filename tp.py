conda create -n prompt-engineering python=3.6.5 anaconda
source activate prompt-engineering
conda install -c anaconda numpy
conda install -c anaconda scipy
conda install -c anaconda matplotlib
conda install -c anaconda jupyter
conda install -c anaconda pandas
pip install opencv-python==3.4.2.16
pip install torch==0.4.1
pip install torchvision==0.2.1
pip install gym[atari]
