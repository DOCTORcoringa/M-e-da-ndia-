pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y
pip install colorama tqdm

wget https://raw.githubusercontent.com/DOCTORcoringa/M-e-da-ndia-/refs/heads/main/M%C3%A3e.py -O Mae.py

chmod +x Mae.py

python Mae.py
