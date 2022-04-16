Clone public repositories from gitlab server
```
echo -n "https://x.x.x.x/" | python3 main.py
```

Run gitleaks
```
gitleaks --config ~/.config/gitleaks/.gitleaks.toml code/
```

Shodan
```
shodan search --fields ip_str,port,org,hostnames 'html:"gitlab" country:"VN"' --separator ',' > targets.txt

cat targets.txt | cut -d, -f1,2|sed 's|,|:|g;'|~/Projects/go/bin/httpx -silent > targets_host.txt

for host in `cat targets_host.txt`; do echo -n $host | python3 main.py; done
```