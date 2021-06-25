#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
export PS1="\[$(tput bold)\]\[\033[38;5;11m\]\w\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;12m\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"
