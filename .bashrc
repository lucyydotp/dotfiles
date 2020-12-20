# ---
# Lucy's Dotfiles
# https://github.com/lucyy-mc/dotfiles-new
# .bashrc
# ---

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

# this lil thingy makes my mc server admin life _so_ much easier
mcdig () {
	dig srv _minecraft._tcp.$1
}

#ps1
export PS1="\[\033[38;5;11m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;14m\]\h\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;12m\]\w\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;13m\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"
