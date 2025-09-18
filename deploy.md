# 🚀 Deploy to Vercel Instructions

## Quick Deployment Steps

### Option 1: GitHub Integration (Recommended)
1. **Go to [vercel.com](https://vercel.com)** and sign in
2. **Click "New Project"**
3. **Import from GitHub**: Select your `Rolling-Strategy-Manager` repository
4. **Configure Project**:
   - Framework: Other
   - Root Directory: `./` (leave default)
   - Build Command: Leave empty (it's a static site)
   - Output Directory: `./` (leave default)
5. **Click "Deploy"**

### Option 2: Vercel CLI (Alternative)
```bash
# In your local project directory
npx vercel

# Follow the prompts:
# - Link to existing project? No
# - What's your project's name? rolling-strategy-manager
# - In which directory is your code located? ./
# - Want to override settings? No

# Deploy to production
npx vercel --prod
```

## 🔧 Live Data Setup (After Deployment)

Once deployed, to get live market data:

1. **Get API Keys**:
   - **Polygon.io**: Sign up at polygon.io (best for options data)
   - **FMP**: Sign up at financialmodelingprep.com
   - **Twelve Data**: Sign up at twelvedata.com (free tier available)
   - **Alpha Vantage**: Sign up at alphavantage.co (free tier available)

2. **Enter API Keys**: 
   - Open your deployed app
   - Enter your API keys in the "API Configuration" section
   - Select your preferred data provider
   - Click "Fetch Live" to get real market data

## 🎯 Features Working Live

✅ **Real-time stock prices**
✅ **Live options pricing** 
✅ **Implied volatility calculation**
✅ **Greeks computation**
✅ **Realistic ML scoring**
✅ **Risk management analysis**

## 📊 Expected Live URL
Your app will be deployed at: `https://rolling-strategy-manager-[random].vercel.app`

## 🛡️ Security Note
API keys are stored locally in your browser and never sent to our servers - they're only used for direct API calls to the market data providers.