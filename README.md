from flask import Flask, request, jsonify
app = Flask(__name__)
LICENSES = {"SHYBAN-CLIENT-123": {"company": "Demo", "requests_left": 10000}}

class Shyban212:
    def search(self, target, left, right):
        steps = 0
        while left <= right:
            steps += 1
            mid = (left + right) // 2
            if mid == target:
                return steps
            elif mid < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

@app.route("/search", methods=["POST"])
def search_api():
    data = request.get_json()
    s = Shyban212()
    steps = s.search(data["target"], data["left"], data["right"])
    return jsonify({"steps": steps})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)







    
