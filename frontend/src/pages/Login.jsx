import { useState } from "react";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div>
      <h2>Login</h2>

      <input placeholder="Username" onChange={(e)=>setUsername(e.target.value)} />
      <br />

      <input type="password" placeholder="Password" onChange={(e)=>setPassword(e.target.value)} />
      <br />

      <button>Login</button>

      <p onClick={()=>window.location.href="/signup"}>Go to Signup</p>
    </div>
  );
}

export default Login;