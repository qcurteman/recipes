# recipes 

# Frontend

## Setup

1. Change to the `react-app` directory
2. Run 
```
npm install
```

## Development
1. Start the server
```
npm run dev
```

## Deployment
Push code to `main`


# Backend

## Setup
1. Setup local python env. This app is running on Python 3.9.13.
```
python3 -m venv venv
```
2. Activate local env:
```
venv\Scripts\activate
```
3. Install packages
```
pip install -r requirements.txt
```
4. Start the server
```
python app.py
```

## Development
1. Activate local env:
```
venv\Scripts\activate
```
2. Start the server
```
python app.py
```

## Deployment

### Deploy
`zappa deploy dev`

### Update Deployment
`zappa update dev`
