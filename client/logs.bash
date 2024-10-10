export HISTFILE="$HOME/.bash_history"

if [ -e "$HOME/.bash_history" ]; then
    if [ -s "$HOME/.bash_history" ]; then
        export HISTFILE="$HOME/.bash_history"
    fi
fi

if [ -e "$HOME/.zsh_history" ]; then
    if [ -s "$HOME/.zsh_history" ]; then
        export HISTFILE="$HOME/.zsh_history"
    fi
fi

cat "$HISTFILE" | tail -n 100 | awk -F ';' '{print $2}' | sed 's/^ *//;s/ *$//' > logs.txt