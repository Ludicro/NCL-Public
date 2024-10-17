#!/bin/zsh

typeset -A assoc_array
flag=('start' 'rev' 'Zt0U' 'd- 46esab' 'c4c48435' 'p- r- dxx' 0 '"4-09-5" "9-0" rt' 1 '"4-09-5" "9-0" rt' 0 '"4-09-5" "9-0" rt' 9 '"4-09-5" "9-0" rt')

vared -p "What is the flag? " -c input
input=("${(@s/-/)input}")
input[3]=("${(@s//)input[3]}")

inc=1
for i j in "${(@kv)flag}"; do
  if [ "$i" = "start" ]; then
    continue
  fi

  res=$(eval "echo "$i" | ${flag[2]} | $(eval echo "$j" | ${flag[2]})")

  echo $res

  if [ "$res" = "$input[$inc]" ]; then
    ((inc++))
    continue
  else
    echo "Wrong Flag!"
    exit
  fi
done

echo "That's the correct flag!"
