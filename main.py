from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/api')
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
  
    current_day = datetime.datetime.now().strftime("%A")

    utc_time = datetime.datetime.utcnow()

    github_file_url = "https://github.com/username/repo/main/file_name.ext"

    github_repo_url = "https://github.com/username/repo"

    status_code = 200

    response_data = {
      "slack_name": slack_name,
      "current_day": current_day,
       "utc_time": utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
       "track": track,
       "github_file_url": github_file_url,
       "github_repo_url": github_repo_url,
        "status_code": status_code
    }
    
    return jsonify(response_data)

if __name__ == "__main__":
    app.run()
