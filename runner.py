from src.intent_web_service import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)