const axios = require('axios');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  const { symbol, endpoint, apiKey, strike, expiry, optionType } = req.query;

  if (!apiKey) {
    return res.status(400).json({ error: 'API key required' });
  }

  try {
    let url;
    
    switch(endpoint) {
      case 'stock':
        url = `https://api.polygon.io/v2/aggs/ticker/${symbol}/prev?apiKey=${apiKey}`;
        break;
      case 'quote':
        url = `https://api.polygon.io/v3/quotes/${symbol}?apiKey=${apiKey}`;
        break;
      case 'option':
        const dateStr = expiry.replace(/-/g, '').substring(2);
        const strikeStr = (parseFloat(strike) * 1000).toString().padStart(8, '0');
        const optionSymbol = `O:${symbol}${dateStr}${optionType}${strikeStr}`;
        url = `https://api.polygon.io/v2/last/trade/${optionSymbol}?apiKey=${apiKey}`;
        break;
      default:
        return res.status(400).json({ error: 'Invalid endpoint' });
    }

    const response = await axios.get(url);
    res.status(200).json(response.data);
    
  } catch (error) {
    console.error('Polygon API error:', error.response?.data || error.message);
    res.status(error.response?.status || 500).json({ 
      error: error.response?.data || error.message 
    });
  }
};
