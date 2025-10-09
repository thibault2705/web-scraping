web-scraping/toronto_az_child_care_centres
# Toronto A - Z Child Care Centres

This is a Python program that scrapes [A - Z list of Licensed Child Care Centres from toronto.ca](https://www.toronto.ca/data/children/dmc/a2z/a2za.html).

## README
### Scraping
**Step 1.** Scrape all child care centres name and link, listed in the page *A - Z list of Licensed Child Care Centres*.

**Step 2.** Scrape all child care centres detail in the link found at previous step.

**Step 3.** Clean and extract information.
- Address info section can be extracted to
  - address
  - cross_street_reference
  - ward

- Phone info section can be extracted to
  - contact_name
  - phone
  - phone_extension
  - email

- Website info section can be extracted to
  - email
    - in case email is unexpectedly input in the website field
  - website
    - standardize website prefix
    - extract website from email if necessary, get rid of email provider to be consider as website *(e.g. gmail.com, hotmail.com, rogers.com)*

**Step 4.** Convert result to DataFrame and export CSV.

<br/>

### Example
[Miles Nadal Community Centre Nursery School](https://www.toronto.ca/data/children/dmc/webreg/gcreg6638.html)


| name | address | cross_street_reference | ward | contact_name | phone | phone_extension| email| website |
|---|---|---|---|---|---|---|---|---|
|Miles Nadal Community Centre Nursery School|750 Spadina Ave|Bloor / Spadina|University-Rosedale|Cheri Szereszewski|416-924-6211|6119||mnjcc.org|

<br/>

[Princess Margaret Nursery School](https://www.toronto.ca/data/children/dmc/webreg/gcreg6459.html)

| name | address | cross_street_reference | ward | contact_name | phone | phone_extension| email| website |
|---|---|---|---|---|---|---|---|---|
|Princess Margaret Nursery School|70 Princess Anne Cres|Eglinton Ave W Trl / Islington|Etobicoke Centre|Kevin Ribeiro|416-889-9403||princessmargaretns@hotmail.com||

<br/>

[Little Giants](https://www.toronto.ca/data/children/dmc/webreg/gcreg14550.html)

| name | address | cross_street_reference | ward | contact_name | phone | phone_extension| email| website |
|---|---|---|---|---|---|---|---|---|
|Little Giants|38 Forest Manor Rd, A|Don Mills Rd./ Sheppard Ave E|Don Valley North|Blessy Simbulan|416-908-3061||info@littlegiants-childservices.com|littlegiants-childservices.com|
<br/>

[Taylor Creek Public School, Extended Day Program](https://www.toronto.ca/data/children/dmc/webreg/gcreg11374.html)

| name | address | cross_street_reference | ward | contact_name | phone | phone_extension| email| website |
|---|---|---|---|---|---|---|---|---|
|Taylor Creek Public School, Extended Day Program|644 Warden Ave|Danforth Road / Warden Avenue|Scarborough Southwest||416-394-2072|edp@tdsb.on.ca||tdsb.on.ca/earlyyears/extended-day-program|
