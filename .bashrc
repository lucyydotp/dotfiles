# ---
# Lucy's Dotfiles
# https://github.com/lucyy-mc/dotfiles-new
# .bashrc
# ---

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias wine32="WINEPREFIX=$HOME/.wine32 WINEARCH=win32 wine"

# this lil thingy makes my mc server admin life _so_ much easier
mcdig () {
	dig srv _minecraft._tcp.$1
}

#ps1
export PS1="\[$(tput bold)\]\[\033[38;5;10m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;12m\]\H\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;13m\]\w\[$(tput sgr0)\] \\$ \[$(tput sgr0)\]"
