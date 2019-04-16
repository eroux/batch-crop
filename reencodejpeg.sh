shopt -s globstar
alljpg="$(find output/ -name \*.jpg -type f | sort)"
for i in $alljpg ; do
	/home/eroux/softs/mozjpeg/jpegtran "$i" | sponge "$i"
done