sed -i -E 's/(\(s-+[-[0-9]+\))//g' memberships.csv
sed -i -E 's/([a-z]+,")//g' memberships.csv
sed -i -E 's/([DEL:0-9a-z-]+)//g' memberships.xlsx