**PRE REQS TO USE THE MLOPS TEMPLATE**


**Install WSL as follows in powershell:**
```powershell
wsl --install
```

**Update WSL and upgrade**
```bash
sudo apt update && sudo apt upgrade
```

**Install the following packages:**
```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```

**Install pyenv**
```bash
curl -k https://pyenv.run | bash
```

**Open .bashrc or .zshrc file**
```bash	
echo $HOME
nano ~/.bashrc
```

**Add the following lines at the end of your .bashrc or .zshrc file**
```bash
# Pyenv configuration
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

**Load the .bashrc or .zshrc file**
```bash
source ~/.bashrc
```

**Install python 3.11.10**
```bash
pyenv install 3.11.10
```

**Set python 3.11.10 as the global version**
```bash
pyenv global 3.11.10
```

**Check the python version**
```bash
python --version
```