# Quick Start

## Run It Directly

### Step 1

- python3
- python lib `requests`

```
pip install requests
```

### Step 2
- Add a new file `config.json` in `/src` and add your environments here:

```
{
  "mail_host": "smtp.***.com",
  "mail_user": "***@***.com",
  "mail_password": "***",
  "receivers": [
    "***@***.com",
    "***@***.com"
  ]
}
```

### Step 3
- Run `/src/report_aqi.sh`

## Using Docker Image

- Pull Image
`docker pull darkery/aqi_report:v1`

- `docker run darkery/aqi_report:v1`

- Add a new file `config.json` in `/project` and add your environments here:

```
{
  "mail_host": "smtp.***.com",
  "mail_user": "***@***.com",
  "mail_password": "***",
  "receivers": [
    "***@***.com",
    "***@***.com"
  ]
}
```
