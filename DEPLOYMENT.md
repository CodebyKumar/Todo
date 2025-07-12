# Deployment Guide

## Quick Deploy to Render

1. **Push your code to GitHub**
2. **Go to [Render](https://render.com) and sign in**
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repo**
5. **Configure:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
6. **Deploy!**

## Environment Variables (Optional)

Set these in Render's dashboard:
- `DEBUG=false` (for production)

## What happens automatically:

- ✅ Port is automatically configured via Render's `PORT` env var using `os.environ.get('PORT', 5000)`
- ✅ Host is set to `0.0.0.0` for external access
- ✅ Debug mode can be controlled via `DEBUG` env var
- ✅ Dependencies are installed from `requirements.txt`

## Port Configuration

The app uses the standard Render port configuration:
```python
port = int(os.environ.get('PORT', 5000))
```

This ensures:
- **Local development**: Uses port 5000
- **Render deployment**: Uses Render's assigned PORT automatically

## Local Development vs Production

**Local (default):**
- Port: 5000 (from default fallback)
- Debug: True
- Reload: True

**Production (Render):**
- Port: Automatically assigned by Render
- Debug: False (if DEBUG=false is set)
- Reload: False

Your API will be available at: `https://your-service-name.onrender.com`
