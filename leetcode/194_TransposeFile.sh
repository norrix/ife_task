awk ' \
{ \
    for(i=1; i<=NF; ++i){ \
        if (word[i] == "") { word[i] = $i } \
        else { word[i] = word[i]" "$i } \
    } \
} END{for(i=1; i<=NF; ++i) {print word[i]}} \
' file.txt