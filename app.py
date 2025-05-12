from flask import Flask, request, jsonify
from db import sql

app = Flask(__name__)

@app.route('/assign-player', methods=['POST'])
def assign_player():
    data = request.json
    player_name = data.get("playerName", "").strip()
    player_id = data.get("id")
    code = data.get("code")

    if not player_name:
        return jsonify({"error": "Player name is required"}), 400

    try:
        if player_id:
            result = sql("""
                UPDATE player_assignments
                SET player_name = ?, code = ?
                WHERE id = ?
                RETURNING id, player_name, team_id, code, created_at
            """, (player_name, code, player_id))
            return jsonify({"assignment": result[0]})
        else:
            team = sql("SELECT id, code FROM teams ORDER BY RANDOM() LIMIT 1")
            if not team:
                return jsonify({"error": "No team found"}), 400
            team_id, team_code = team[0]['id'], team[0]['code']
            unique_code = f"{team_code}{str(hash(player_name))[:4]}"
            new_assignment = sql("""
                INSERT INTO player_assignments (player_name, team_id, code)
                VALUES (?, ?, ?)
                RETURNING id, player_name, team_id, code, created_at
            """, (player_name, team_id, unique_code))
            return jsonify({"assignment": new_assignment[0]})
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
