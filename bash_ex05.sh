sourse = $1
dest = $2

if [["$sourse" -eq "$dest"]]
then
echo "Применик $dest и источник $sourse один и тот же файл!"
exit 1
else
cp $sourse $dest
echo "Удачное копирование!"
fi
