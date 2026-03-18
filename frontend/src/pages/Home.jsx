function Home() {
  return (
    <div>
      <h2>Home Page</h2>

      <button onClick={()=>window.location.href="/vote/1"}>Go to Vote</button>
      <button onClick={()=>window.location.href="/results/1"}>View Results</button>
    </div>
  );
}

export default Home;