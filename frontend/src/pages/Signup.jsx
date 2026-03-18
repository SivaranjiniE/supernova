import { useState } from "react";

function Signup() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div>
      <h2>Signup</h2>

      <input placeholder="Username" onChange={(e)=>setUsername(e.target.value)} />
      <br />

      <input type="password" placeholder="Password" onChange={(e)=>setPassword(e.target.value)} />
      <br />

      <button>Signup</button>
    </div>
  );
}

export default Signup;