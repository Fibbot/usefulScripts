## quick n dirty recon script
## chmod +x recon.sh
## export target=target.com
## export GITHUB_API_KEY=key
## mkdir $target
## cd $target && $_
## mkdir subdomainResults
## export subdomains=`pwd`/subdomainResults
## uniqthis:
#uniqthis(){
#	ab=${PWD}
#	bc=$1
#	tr A-Z a-z < $bc > $ab/abc
#	sort $ab/abc > $ab/def
#	awk '!visited[$0]++' $ab/def > $ab/$bc
#	rm $ab/abc
#	rm $ab/def
#}
## run with: source recon.sh

subfinder -d $target -silent | tee $subdomains/subfinder-$target
amass enum --passive -d $target -o $subdomains/amass-$target --config ~/config.ini
assetfinder -subs-only $target | tee $subdomains/assetfinder-$target
subdomainizer -u $target -g -gt $GITHUB_API_KEY -o $subdomains/subdomainizer-$target
cat $subdomains/*$target >  $subdomains/total-subdomains
cd $subdomains
uniqthis total-subdomains
mv total-subdomains ../
cd ../
httpx -l total-subdomains -title -status-code -silent -no-color -json -o httpxResults
cat  httpxResults | grep -v 404 | grep -v 500| tee -a aliveDomains
cat aliveDomains | jq -r .url | tee aliveDomainsURL
cat aliveDomainsURL | sed -e 's/^http:\/\///g' -e 's/^https:\/\///g' | tee aliveDomainsNoHTTP
naabu -silent -rate 500 -hL aliveDomainsNoHTTP -json -o portScan
mkdir aquatone && cd $_
cat ../aliveDomainsURL | aquatone