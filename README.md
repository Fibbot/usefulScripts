stuff i've found to be useful in pentesting or bug bounties

# slowCurlAnnoyingDomains
- when using amass/massdns sometimes you'll get a massive list of domains that all redirect to the same site like:
- '1.abc.com, 2.abc.com, stupid.abc.com' --> abc.com
- this will (slowly) go through that list spitting out the final site
- once you get the results outfile, you can uniq it to find any true subdomains
- i know this can be done faster, but i've had the issue of being blocked (429 error) by cloudflare and the like when running too fast
# simpleSUID
- usually used when we've been able to get root on a box and want a quick/easy way to re-root
# permCheck
- finding folder permissions, usually on a giant nfs
# azureLoot
- quick checking azure client tokens