#!/bin/bash
# Check external links used on the site (exclude afetoncesi.com)
urls=(
  "https://www.turkiye.gov.tr/afet-ve-acil-durum-yonetimi-acil-toplanma-alani-sorgulama"
  "https://www.afad.gov.tr/afet-haritalari"
  "https://www.112.gov.tr/"
  "https://www.dask.gov.tr/"
  "https://www.afad.gov.tr/afadem/sel"
  "https://www.afad.gov.tr/afet-ve-acil-durum-cantasi-nasil-hazirlanmali"
  "https://www.afad.gov.tr/afete-hazir-turkiye"
  "https://www.kizilay.org.tr/"
  "https://www.afad.gov.tr/"
  "https://www.afad.gov.tr/afadem"
  "https://deprem.afad.gov.tr/"
  "https://www.mgm.gov.tr/meteouyari/turkiye.aspx"
  "https://www.mgm.gov.tr/"
  "https://www.tsunami.gov/?page=tsunamiFAQ"
  "https://www.afad.gov.tr/afadem/deprem"
  "https://www.afad.gov.tr/afadem/deprem"
  "https://www.afad.gov.tr/e-devlet-uygulamalarimiz"
  "https://www.afad.gov.tr/afadem/yangin"
  "https://www.afad.gov.tr/afadem/cig"
  "https://www.afad.gov.tr/hortum-afetinde-alabileceginiz-onlemleri-biliyor-musunuz23"
  "https://www.afad.gov.tr/afad-meteoroloji-uyarisi-basin-bulteni"
  "https://www.afad.gov.tr/afadem/heyelan"
  "https://www.afad.gov.tr/yildirim-tehlikesine-karsi-neler-yapilmali"
  "https://www.afad.gov.tr/afad-kuvvetli-yagislara-karsi-uyariyor"
)
for u in "${urls[@]}"; do
  code=$(curl -sI -L -o /dev/null -w "%{http_code}" --connect-timeout 10 "$u" 2>/dev/null || echo "ERR")
  echo "$code $u"
done
